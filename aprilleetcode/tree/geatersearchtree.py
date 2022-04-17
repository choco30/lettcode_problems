#goal is to remove convert the binary serch tree in to grester search tree , where each node value is the sum between  
#all the greater value of node with the node value
#approach is to perform recuursion from right side and than left side as greater value is on the right side,then just add it into the variablea nd sum it with the current value
#of node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.add=0
        if root is None:
            return root 
        def gst(root):
            if root is None:
                return 0
            gst(root.right)
            value=root.val
            root.val=root.val+self.add
            self.add+=value
            gst(root.left)
            print(self.add,root.val)
            return root
        return gst(root)
            
