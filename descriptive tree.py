# leetcode 2196
#to form a binary tree from a list of list within a list refer to question
# approach is to create a dictionary of tree nodes where dic key is node value  and dictionary value is tree node
#for parent node if node not in dic enter it same for child but also enter the value of child in dictionary to get the tree node as the node which is not in child node will be root node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic=dict()
        child={}
        
        for j in descriptions:
            temp=None
            if j[0] not in dic:
                dic[j[0]]=TreeNode(j[0],None,None)
                temp=dic[j[0]]
            else:
                temp=dic[j[0]]
            if j[1] not in dic:
                dic[j[1]]=TreeNode(j[1],None,None)
                if j[2]==1:
                    temp.left=dic[j[1]]
                else:
                    temp.right=dic[j[1]]
                child[j[1]]=1
            else:
                child[j[1]]=1
                if j[2]==1:
                    temp.left=dic[j[1]]
                else:
                    temp.right=dic[j[1]]

        
        for i in dic:
            if i not in child:
                print(i)
                return dic[i]
 
 
                
                
            
        
