# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output=0
    def findsum(self,root):
        if root==None:
            return
        if root.left:
            if (root.left).left==None and (root.left).right==None:
                self.output+=root.left.val
            else:
                self.findsum(root.left)
        self.findsum(root.right)
        
        
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return None
        self.findsum(root)
        return self.output
        
            
        