from queue import PriorityQueue 
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq=PriorityQueue()
        dic=dict()
        size=len(mat)
        row=-1
        for i in (mat):
            count=0
            row+=1
            for j in i:
                if j==1:
                    count+=1
            if count in dic:
                lis=dic.get(count)
                lis.append(row)
                dic[count]=lis
            else:
                lis=[]
                lis.append(row)
                dic[count]=lis
        li=list(dic.keys())
        a=[]
        li.sort()
        for i in li:
            a.extend(dic[i])
        return a[:k]
