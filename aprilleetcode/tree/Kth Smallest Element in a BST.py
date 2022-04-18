#to find the kth smallest element
#approach traverse the node in preorder treversal and store all the element in the list
#and then return the k-1th elemnt from the list
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ele=[]
        def find(root):
            if root is None:
                return 
            find(root.left)
            ele.append(root.val)
            find(root.right)
            return ele
        a=find(root)
        print(a)
        return a[k-1]
        
