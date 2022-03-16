# leetcode 946
# approach to find weather the given two list are valid stack push and pop operation
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        size=len(pushed)
        left=0
        stack=[]
        right=0
        for i in range(size):
            stack.append(pushed[i])
            if pushed[i]==popped[right]:
                left=len(stack)-1
                while left>=0 and stack[left]==popped[right]  and right<size:
                    stack.pop()
                    right+=1
                    left-=1
                print(stack)    
        return True if len(stack)==0 else False
                   
