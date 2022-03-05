# Need to select a number such that no-1 and no+1 will not  be selected
#Approach to first get the value for a total value of a particular no in an array
# to form an array by selecting max of last value or two pos earlier value + current value(as no-1 is not allowded)
#and the max value is find at the lkarest no in the array
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        size=len(nums)
        dic={}
        maxno=-1
        for i in nums:
            if i>maxno:
                maxno=i
            if dic.get(i,0):
                dic[i]+=i
            else:
                dic[i]=i
        
        dp=[0]*(maxno+1)
        dp[0]=dic.get(0,0)
        dp[1]=dic.get(1,0)
        for i in range(2,maxno+1):
            dp[i]=max(dp[i-1],dp[i-2]+dic.get(i,0))
        return dp[maxno]
        
        
