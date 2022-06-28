# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output=0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root==None:
            return 0
        def findpath(root, targetSum ):
            if root==None:
                return
            if root.val==targetSum:
                self.output+=1
            targetSum-=root.val
            findpath(root.left, targetSum)
            findpath(root.right, targetSum)
            return 
        findpath(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.output
            
                
            
        