# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        if root==p or root==q:
            return root
        left_search=self.lowestCommonAncestor(root.left,p,q)
        right_search=self.lowestCommonAncestor(root.right,p,q)
        if left_search==None and right_search==None:
            return None
        if left_search==None:
            return right_search
        if right_search==None:
            return left_search
        if ((left_search==p and right_search==q) or (left_search==q and right_search==p)):
            return root
        return
        
        