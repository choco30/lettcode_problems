#day 30
#74. Search a 2D Matrix
#Approach-To check each row if the end elemen is greater than target since rows are sorted , if last elemt of row i9s smaller 
#continue with new row otherwise search the current row, simple binary search on each row,so it will give o(n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        colums=len(matrix[0])
        for i in (matrix):
            if(i[colums-1]<target):
                continue
            else:
                left=0
                right=len(i)-1
                while(left<=right):
                    mid=left+(right-left)//2
                    if i[mid]==target:
                        return True
                    elif i[mid]>target:
                        right=mid-1
                    elif i[mid]<target:
                        left=mid+1
        return False                
