# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxTree(self,nums, l, h):
    #     n=len()
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n=len(nums)
        
        if n==0:
            return None
        root=None
        i=nums.index(max(nums))
        val=max(nums)
        root=TreeNode(val)
        root.left=self.constructMaximumBinaryTree(nums[:i])
        root.right=self.constructMaximumBinaryTree(nums[i+1:])
        return root
        
        