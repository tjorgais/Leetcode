# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.list1=[]
    def inorder(self, root):
        if root==None:
            return 
        self.inorder(root.left)
        self.list1.append(root.val)
        self.inorder(root.right)
        return
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:
            return None
        self.inorder(root)
        return self.list1[k-1]
        
        
        