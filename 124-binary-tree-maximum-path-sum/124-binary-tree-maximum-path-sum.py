# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.hist=-3*10^8
    def maxpath(self,root):
        if root==None:
            return 0
        left_sum=self.maxpath(root.left)
        right_sum=self.maxpath(root.right)
        max_path=max(max(left_sum,right_sum)+root.val,root.val)
        max_top=max(max_path, left_sum+right_sum+root.val)
        self.hist=max(max_top,self.hist)
        return max_path
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxpath(root)

        return self.hist
        
        