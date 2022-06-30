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
    def ConvertBinary(self, l, r):
        if l>r:
            return None
        root=None
        i=((r-l)//2)+l
        root=TreeNode(self.list1[i])
        root.left=self.ConvertBinary(l,i-1)
        root.right=self.ConvertBinary(i+1,r)
        return root
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        self.inorder(root)
        n=len(self.list1)
        
        root=self.ConvertBinary(0,n-1)
        return root
        
        