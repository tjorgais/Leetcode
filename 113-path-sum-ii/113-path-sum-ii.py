# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output=[]
    def findpath(self, root, targetSum, path, count):
        if root==None:
            return 
        count+=root.val
        path.append(root.val)

        if root.left==None and root.right==None:
            if count==targetSum:
                
                self.output.append(path.copy())
        
        self.findpath(root.left,targetSum, path, count)
        self.findpath(root.right, targetSum, path, count)
        path.pop()
        return 
        
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root==None:
            return None
        path=[]
        count=0
        self.findpath(root,targetSum, path, count)
        return self.output
        
        