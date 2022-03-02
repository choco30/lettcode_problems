
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0 and len(t)==0:
            return True      
        elif len(t)==0:
            return False
        elif  len(s)==0:
            return True
       
        cmp=0
        for i in t:
            if s[cmp]==i:
                if cmp==len(s)-1:
                    return True
                else:
                    cmp+=1
        return False            
        
        
        
