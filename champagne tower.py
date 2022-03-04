# to find the content of champagne at given glass in a given row

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        left=poured
        if poured==0:
            return poured
        li=[[0]* for i in range(1,102)]  #maximum row given
        li[0][0]=poured   
        for i in range(query_row+1):
          for j in range(i+1):
            glass_content=(li[i][j]-1)/2    # a particular glass overflows left champagne -1  which is distibuted in ts left and right  so divide by 2
            if glass_content>0:
              li[i+1][j]+=glass_content          # filling left child of the current cup
              li[i+1][j+1]=glass_content         # filling right child of the current cup   
        return min(1,li[quer_row][query_glass])  #since a glass can only contain minimum 1 unit of champagne
      
