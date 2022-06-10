# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def countgood(root, Max):
    if not root:
        return 0
    
    elif root.val>=Max:
        Max=max(root.val, Max)
        return countgood(root.left,Max)+countgood(root.right,Max)+1
    else:
        return countgood(root.left,Max)+countgood(root.right,Max)
    
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_count=0
        right_count=0
        if root.left:
            left_count=countgood(root.left, root.val)
        if root.right:
            right_count=countgood(root.right, root.val)
        print(left_count)
        print(right_count)
        return left_count+right_count+1
            
        