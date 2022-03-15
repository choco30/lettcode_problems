#to remove the extra paranthesis from the string
# approach iterate string two time 
#for firat time if closing parenthesis are grater than opening parenthesis so string is not balanced skit it
# for second loop treverse from last look if for an index if opening braces are geater than closing parenthesis
#return the reverse of string

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openc=0
        closec=0
        res=""
        size=len(s)
        for i in s:
            if i=="(":
                openc+=1
            elif i==")":
                closec+=1
            if closec>openc:
                closec-=1
                continue
            res=res+i    
        print(res)
        s=res
        openc,closec,res=0,0,""
        for i in s[-1::-1]:
            if i=="(":
                openc+=1
            elif i==")":
                closec+=1
            if openc>closec:
                openc-=1
                continue
            res=res+i              
        return res[-1::-1]    
