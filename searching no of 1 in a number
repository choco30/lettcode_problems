class Solution:
    def countBits(self, n: int) -> List[int]:
        dic={}
        lis=[]
        for i in range(n+1):
            temp=str(bin(i))
            dic=Counter(temp)
            lis.append(dic.get("1",0))
        return lis    
