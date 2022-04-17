#goal is to remove the value from bst which are not in limit, if value of node is greater than upper bound
#return its left tree, if value is lower than the lower klimit, return right tree , if it is in the value do recurrsion on let and right tr
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(low,high,root):
            if root is None:
                return None
            if root.val>high:
                return trim(low,high,root.left)
            if root.val<low:
                return trim(low,high,root.right)
            root.left=trim(low,high,root.left)
            root.right=trim(low,high,root.right)
            return root
        
        return trim(low,high,root)                    
