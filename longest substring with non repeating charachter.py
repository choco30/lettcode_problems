'''leetcode 3
To find the longest subs tring with non repaeting character
making a dynamic window where we store each charchter along with its index in a dictionary and update it when we a find repeating value
we take two pointers left and right which act as an oppossite end of a active window  where we update our left if we find a repeating charater we look for the earliwer occurence of 
of that character in the dictionary and if it is greater than the curret index of left than we assign its value to left  do a max of earlier string length to current string length and return the answer
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size=len(s)
        dic=dict()
        left=0
        right=0
        length=0
        for i in range(size):
            right=i
            if s[i] in dic:
                left=max(dic[s[i]]+1,left)
            dic[s[i]]=i    
            length=max(length,right-left+1)    
        return length
            
                    
            

                

            


            
                    
            

                

            
