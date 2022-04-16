A simple serach of value in bst, if node value is greater than value call recurrsion on the left hand node and vice versa when matched return head or return none if not found

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head=root
        value=val
        def find(head,value):
            if head is None:
                return None
            if value==head.val:
                return head
            elif value>head.val:
                return find(head.right,value)
            elif value<head.val:
                return find(head.left,value)
                
        z= find(root,val)        
        print(z)
        return z
