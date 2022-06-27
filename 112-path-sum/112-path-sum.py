# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checksum(self, root, targetSum, output):
        if root==None:
            return False
        if root.left==None and root.right==None:
            if root.val+output==targetSum:
                return True
        output+=root.val
        return self.checksum(root.left, targetSum,output) or self.checksum(root.right, targetSum,output)
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False
        output=0
        return self.checksum(root, targetSum, output)
        