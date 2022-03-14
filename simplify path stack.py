#simplify path leetcode 71 problem on stack
#performing push and pop in stack ds

class Solution:
    def simplifyPath(self, path: str) -> str:
        lis=path.split("/")
        stack=[]
        print(lis)
        for i in lis:
            if i not in['','.','..']:
                stack.append(i)
            elif i == ".." and len(stack)!=0:
                stack.pop()
                print(stack)
        return "/"+"/".join(stack)        
