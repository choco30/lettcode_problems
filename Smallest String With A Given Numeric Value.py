class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        word=""
        sums=k
        for i in range(n):
            letter='a'
            sums=sums-1
            while (n-(i+1))*26<sums:
                letter=chr(ord(letter)+1)
                sums=sums-1
            word+=letter
        return word
