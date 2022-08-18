from datetime import timedelta,datetime
from google.cloud import storage
from google.cloud.storage import bucket
from airflow import DAG
import gcsfs
import openpyxl
import pandas as pd
import numpy as np
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.contrib.operators import gcs_to_bq
from airflow.operators import python_operator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators import gcs_delete_operator
from airflow.models import Variable
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
from google.cloud import bigquery


finance_email_config = Variable.get("finance_email_config", deserialize_json=True)
email_list=finance_email_config["brand_promo_email_list"] 

common_var = Variable.get("common_config", deserialize_json=True) 
BQ_CONN_ID=common_var["BQ_CONN_ID"]
BQ_PROJECT=common_var["BQ_PROJECT"]
location=common_var["location"]
BQ_stg_dataset=common_var["BQ_stg_dataset"]
BQ_raw_dataset = common_var["BQ_raw_dataset"]



brand_promo_config=Variable.get("brand_promo_config", deserialize_json=True)
budget_load_bucket=brand_promo_config["budget_load_bucket"]
Amor_PS_OE_FME_GST_BUDGET_Table=brand_promo_config["Amor_PS_OE_FME_GST_BUDGET_Table"]
TPT_BUDGET_Table=brand_promo_config["TPT_BUDGET_Table"]
temp_brand_promo_TPT_BUDGET_table=brand_promo_config["temp_brand_promo_TPT_BUDGET_table"]
temp_Amor_PS_OE_FME_GST_BUDGET_TABLE=brand_promo_config["temp_Amor_PS_OE_FME_GST_BUDGET_TABLE"]
brand_pnl_sales_archive=brand_promo_config["brand_pnl_sales_archive"]

cur_date= datetime.now()

DEFAULT_ARGS = {
    'depends_on_past': False,
    'start_date': datetime.today() - timedelta(1),
    'email_on_failure': True,
    'email_on_retry': False,
    'email': email_list,
    'catchup': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG('brand_promo_budget',
    default_args=DEFAULT_ARGS,
    schedule_interval = None,
    catchup=False,
)

def extract_csv_from_excel():
    fs = gcsfs.GCSFileSystem(project=BQ_PROJECT)
    file_list = fs.ls(budget_load_bucket)
    excel_file = [f for f in file_list if f.endswith('.xlsx')]
    excel_file = excel_file[0]

    Budget_TPT_sheet="TPT@SKU_ Budget_yr"
    BUdget_combine_sheet="Amor_PS_OE_FME_GST@brand_Budget"
    
    df = pd.read_excel('gs://' + excel_file, engine='openpyxl',sheet_name=Budget_TPT_sheet)
    df.to_csv('gs://'+budget_load_bucket+'/'+Budget_TPT_sheet+'.csv',index=False)
    df = pd.read_excel('gs://' + excel_file, engine='openpyxl',sheet_name=BUdget_combine_sheet)
    df.to_csv('gs://'+budget_load_bucket+'/'+BUdget_combine_sheet+'.csv',index=False)

def my_func():
    bq_client=bigquery.Client()
    query=''' select distinct(left(partition_year,4)) from (SELECT *,cast(date_add(CAST(CONCAT(CAST(CALENDAR_YEAR as STRING),"-",
        CASE WHEN LENGTH(CAST(CALENDAR_MONTH as STRING)) = 1 THEN CONCAT('0', CAST(CALENDAR_MONTH as STRING))
        when LENGTH(CAST(CALENDAR_MONTH as STRING)) = 2 THEN CAST(CALENDAR_MONTH as STRING)
        END,'-01' ) as DATE) ,Interval 9 MONTH) as String) as partition_year  FROM `finance-dcube-prod.stg_table_prod.temp_brand_promo_TPT_BUDGET`)''' 
    query_run=bq_client.query(query)
    partition_year=""
    for row in query_run:
        partition_year=row[0]
    return partition_year

Excel_to_CSV= PythonOperator(
    task_id='Excel_to_CSV', 
    python_callable=extract_csv_from_excel,
    email_on_failure = True,
    dag=dag
)

BRAND_PROMO_DATE_FUNCTION = PythonOperator(
    task_id='BRAND_PROMO_DATE_FUNCTION',
    python_callable=my_func,
    email_on_failure=True,
    dag=dag
)

BRAND_PROMO_FINANCE_Budget_TPT_LOAD_TASK = gcs_to_bq.GoogleCloudStorageToBigQueryOperator(
    task_id='BRAND_PROMO_FINANCE_Budget_TPT_LOAD_TASK',
    bucket=budget_load_bucket,
    source_objects=['TPT@SKU_ Budget_yr.csv'],
    destination_project_dataset_table=BQ_PROJECT+"."+BQ_stg_dataset+"."+temp_brand_promo_TPT_BUDGET_table,
    skip_leading_rows = 1,
    schema_object = 'TPT_Budget_Data_schema.json',
    write_disposition = 'WRITE_TRUNCATE',
    email_on_failure = True,
    dag=dag)

BRAND_PROMO_FINANCE_Budget_GST_LOAD_TASK = gcs_to_bq.GoogleCloudStorageToBigQueryOperator(
    task_id='BRAND_PROMO_FINANCE_Budget_GST_LOAD_TASK',
    bucket=budget_load_bucket,
    source_objects=['Amor_PS_OE_FME_GST@brand_Budget.csv'],
    destination_project_dataset_table=BQ_PROJECT+"."+BQ_stg_dataset+"."+temp_Amor_PS_OE_FME_GST_BUDGET_TABLE,
    skip_leading_rows = 1,
    schema_object = 'Amor_PS_FME_GST_brand_BUDGET.json',
    write_disposition = 'WRITE_TRUNCATE',
    email_on_failure = True,
    dag=dag)


layer1_BRAND_PROMO_TPT_BUDGET_LOAD_TASK = BigQueryOperator(
    task_id='layer1_BRAND_PROMO_TPT_BUDGET_LOAD_TASK',
    destination_dataset_table = BQ_PROJECT+"."+BQ_raw_dataset+"."+TPT_BUDGET_Table + "$"+ "{{task_instance.xcom_pull(task_ids='BRAND_PROMO_DATE_FUNCTION') }}",
    write_disposition='WRITE_TRUNCATE',
    sql='''
		SELECT 
        BU,COUNTRY,KPI_NAME,cast(cast(CALENDAR_YEAR as float64)as String) as CALENDAR_YEAR,cast(cast(CALENDAR_MONTH as float64)as String) as CALENDAR_MONTH,
        PROD_ID,DIVISION,AMOUNT,CURRENCY,DATA_SRC,VERSION,
        date_add(CAST(CONCAT(CAST(CAST(CALENDAR_YEAR as FLOAT64)AS STRING),"-",
        CASE WHEN LENGTH(CAST(CAST(CALENDAR_MONTH as FLOAT64)AS STRING)) = 1 THEN CONCAT('0', CAST(CAST(CALENDAR_MONTH as FLOAT64)AS STRING))
        when LENGTH(CAST(CAST(CALENDAR_MONTH as FLOAT64)AS STRING)) = 2 THEN CAST(CAST(CALENDAR_MONTH as FLOAT64)AS STRING)
        END,'-01' ) as DATE) ,Interval 9 MONTH) as partition_year
        FROM {0}.{1}.{2}

		where CALENDAR_YEAR is not Null
		'''.format(BQ_PROJECT,BQ_stg_dataset,temp_brand_promo_TPT_BUDGET_table),
    allow_large_results=True,
    time_partitioning = {'type': 'YEAR','field': 'PARTITION_YEAR','requirePartitionFilter': 'False'},
    use_legacy_sql=False,
    bigquery_com_id=BQ_CONN_ID,
    email_on_failure = True,
    dag=dag
)

layer1_BRAND_PROMO_FINANCE_BUDGET_GST_LOAD_TASK = BigQueryOperator(
    task_id='layer1_BRAND_PROMO_FINANCE_BUDGET_GST_LOAD_TASK',
    destination_dataset_table = BQ_PROJECT+"."+BQ_raw_dataset+"."+Amor_PS_OE_FME_GST_BUDGET_Table+ "$"+ "{{task_instance.xcom_pull(task_ids='BRAND_PROMO_DATE_FUNCTION') }}",
    write_disposition='WRITE_TRUNCATE',
    sql='''
		SELECT BU,COUNTRY,cast(cast(GL AS FLOAT64) as STRING) AS GL ,BRAND,DIVISION,cast(cast(CALENDAR_YEAR as float64)as String) as CALENDAR_YEAR,cast(cast(CALENDAR_MONTH as float64)as String) as CALENDAR_MONTH,AMOUNT,
        CURRENCY,VERSION,   
        date_add(CAST(CONCAT(CAST(CAST(CALENDAR_YEAR as FLOAT64)AS STRING),"-",
        CASE WHEN LENGTH(CAST(CAST(CALENDAR_MONTH as FLOAT64)AS STRING)) = 1 THEN CONCAT('0', CAST(CAST(CALENDAR_MONTH as FLOAT64)AS STRING))
        when LENGTH(CAST(CAST(CALENDAR_MONTH as FLOAT64)AS STRING)) = 2 THEN CAST(CAST(CALENDAR_MONTH as FLOAT64)AS STRING)
        END,'-01' ) as DATE) ,Interval 9 MONTH) as partition_year
        FROM {0}.{1}.{2}

		where CALENDAR_YEAR is not NULL
		'''.format(BQ_PROJECT,BQ_stg_dataset,temp_Amor_PS_OE_FME_GST_BUDGET_TABLE),
    allow_large_results=True,
    time_partitioning = {'type': 'YEAR','field': 'PARTITION_YEAR','requirePartitionFilter': 'False'},
    use_legacy_sql=False,
    bigquery_com_id=BQ_CONN_ID,
    email_on_failure = True,
    dag=dag
)



BRAND_PROMO_FINANCE_ACTUALS_DATA_ARCHIVAL = GCSToGCSOperator(
    task_id="BRAND_PROMO_FINANCE_ACTUALS_DATA_ARCHIVAL",
    source_bucket=budget_load_bucket,
    source_object='*.xlsx',
    destination_bucket=brand_pnl_sales_archive,
    destination_object= "brand_promo_BUDGET/" + str(cur_date),
    dag=dag
)

def BRAND_PROMO_FINANCE_BUDGET_bucket_cleanup_func():
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(budget_load_bucket)
    blobs = bucket.list_blobs()
    xl_blobs = [f for f in blobs if f.name.endswith('.xlsx') or f.name.endswith('.csv')]
    for blob in xl_blobs:
        blob.delete()

BRAND_PROMO_FINANCE_BUCKET_CLEANUP = PythonOperator(
    task_id='BRAND_PROMO_FINANCE_BUCKET_CLEANUP',
    python_callable=BRAND_PROMO_FINANCE_BUDGET_bucket_cleanup_func,
    email_on_failure = True,
    trigger_rule = 'none_failed_or_skipped',
    dag=dag
)

Excel_to_CSV.set_downstream([BRAND_PROMO_FINANCE_Budget_GST_LOAD_TASK,BRAND_PROMO_FINANCE_Budget_TPT_LOAD_TASK,BRAND_PROMO_FINANCE_ACTUALS_DATA_ARCHIVAL])
BRAND_PROMO_DATE_FUNCTION.set_upstream([BRAND_PROMO_FINANCE_Budget_GST_LOAD_TASK,BRAND_PROMO_FINANCE_Budget_TPT_LOAD_TASK])
BRAND_PROMO_DATE_FUNCTION.set_downstream([layer1_BRAND_PROMO_TPT_BUDGET_LOAD_TASK,layer1_BRAND_PROMO_FINANCE_BUDGET_GST_LOAD_TASK])
BRAND_PROMO_FINANCE_BUCKET_CLEANUP.set_upstream([BRAND_PROMO_FINANCE_ACTUALS_DATA_ARCHIVAL,layer1_BRAND_PROMO_FINANCE_BUDGET_GST_LOAD_TASK,layer1_BRAND_PROMO_TPT_BUDGET_LOAD_TASK])
