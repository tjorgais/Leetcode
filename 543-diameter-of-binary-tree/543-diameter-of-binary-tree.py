# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def diamBinTree(root):
    global current_max
    if root.left==None and root.right==None:
        return 1
    elif root.left==None:
        return diamBinTree(root.right)+1
    elif root.right==None:
        return diamBinTree(root.left)+1
    else:
        x=diamBinTree(root.left)
        y=diamBinTree(root.right)
        if x+y>current_max:
            current_max=x+y
        return max(x,y)+1
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global current_max
        current_max=-10^6
        length=diamBinTree(root)
        return max(current_max, length-1)
        
        