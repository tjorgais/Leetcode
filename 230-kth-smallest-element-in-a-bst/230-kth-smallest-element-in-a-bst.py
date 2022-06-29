# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Deletemin(self, root):
        if root==None:
            return None
        if root.left:
            root.left=self.Deletemin(root.left)
            return root
        return root.right
    def findmin(self, root):
        if root==None:
            return None
        if root.left:
            return self.findmin(root.left)
        return root.val
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:
            return None
        i=1
        while(i!=k):
            root=self.Deletemin(root)
            i+=1
        return self.findmin(root)
#     def __init__(self):
#         self.list1=[]
#     def inorder(self, root):
#         if root==None:
#             return 
#         self.inorder(root.left)
#         self.list1.append(root.val)
#         self.inorder(root.right)
#         return
    
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         if root==None:
#             return None
#         self.inorder(root)
#         return self.list1[k-1]
        
        
        