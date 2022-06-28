# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_valid(self,root):
        if root==None:
            return False
        if root.val==1:
            return True
        return self.check_valid(root.left) or self.check_valid(root.right)
        
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return None
        if root.left:
            if self.check_valid(root.left):
                root.left=self.pruneTree(root.left)
            else:
                root.left=None
        if root.right:
            if self.check_valid(root.right):
                root.right=self.pruneTree(root.right)
            else:
                root.right=None
        if root.left==None and root.right==None and root.val==0:
            return None
        return root
        

            