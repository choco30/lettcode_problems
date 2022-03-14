# approach here we need to find the three distict elemnt whose sum ==0 for which which we create left and right pointer for each entry and iterate for each value which is fixed in the whole array and a 2sum after fixing the element
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lis=[]
        size=len(nums)
        for i in range(0,size-2):
            if nums[i]==nums[i-1] and i>0:
                continue
            left=i+1
            right=size-1
            while(left<right):
                no=nums[i]+nums[left]+nums[right]
                if no<0:
                    left+=1
                elif no>0:
                    right-=1
                else:
                    lis.append([nums[left],nums[right],nums[i]])
                    while left<right and nums[left]==nums[left+1]:left+=1
                    while left<right and nums[right]==nums[right-1]:right-=1               
                    left+=1
                    right-=1
                        
        return lis                            
                    
            
        
