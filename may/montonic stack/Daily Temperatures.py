#leetcode problem 739
#approach:Instead of using two loos,we can just iterate over each element of the array , and store the valaue along with 
# its index on a stack  and when we encounter a value greater than tos we just pop it off and  for tos value index we just
#we just store at its index the diff of tos index and current indesx and push current value to the stack.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size=len(temperatures)
        stack=[]
        arr=[0]*size
        stack.append([temperatures[0],0])
        tos=0
        for i in range(1,size):
            while stack:
                tos=len(stack)-1
                if stack[tos][0]<temperatures[i]:
                    index=stack[tos][1]
                    arr[index]=i-index
                    stack.pop()
                else:
                    break
            stack.append([temperatures[i],i])
        return arr            
        
