# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumnum(self, root, num):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            num=num+str(root.val)
            return int(num)
        num=num+ str(root.val)
        return self.sumnum(root.left,num)+self.sumnum(root.right,num)
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        num=""
        return self.sumnum(root,num)
        
        
       
        