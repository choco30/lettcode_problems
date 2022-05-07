#to find the 132  like pattern
#approach:start from the right side appen the elenment into a stack and pop if tos >current element
#taske sl=-infinity and compared the max of tos and already existing value of sl, in this way we wil get the second largest
#and when current element is less than sl print true 
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        size=len(nums)
        stack=[]
        sl=-1*10**9
        stack.append(nums[size-1])
        tos=0
        for i in reversed(range(0,size)):
            while stack:
                if nums[i]<sl:
                    return True
                if stack[tos]<nums[i]:
                    z=stack.pop()
                    tos-=1
                    sl=max(sl,z)
                else:
                    break
            stack.append(nums[i])
            tos+=1
        return False
