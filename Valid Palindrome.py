class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        lis=[]
        for i in s:
            if (ord(i)<=122 and ord(i)>=97) or (ord(i)>=48 and ord(i)<=57):
                lis.append(i)
        size=len(lis)
        if size%2!=0:
            if lis[:size//2:1]==lis[size-1:size//2:-1]:
                return True
            else:
                return False
        else:
            if lis[:size//2:]==lis[size-1:size//2-1:-1]:
                return True
            else:
                return False
