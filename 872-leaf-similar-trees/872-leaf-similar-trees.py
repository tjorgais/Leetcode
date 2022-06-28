# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1=[]
        list2=[]
        def leafseq(root, list1):
            if root==None:
                return list1
            if root.left==None and root.right==None:
                list1.append(root.val)
            leaf1=leafseq(root.left,list1)
            leaf1=leafseq(root.right,list1)
            return list1
        list1=leafseq(root1, list1)
        list2=leafseq(root2, list2)
        if list1==list2:
            return True
        return False
        