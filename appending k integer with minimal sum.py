# to append the k unique integer in the given list which are not part of it and return the inserted nos sum
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        count=0
        nums=set(nums)
        sum=(k*(k+1))//2
        for i in nums:
            if i>=1 and i<=k:
                sum-=i
                count+=1
        i=k+1        
        while count!=0:
            if i not in nums:
                count-=1
                sum=sum+i
            i+=1
        return sum
