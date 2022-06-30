# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkCh(self, root):
        
        return True if root.left and root.right else False
    def NextBigger(self,root):
        if root.left and root.right:
            if root.val==root.left.val and root.left.val==root.right.val:
                mini_left=self.NextBigger(root.left)
                mini_right=self.NextBigger(root.right)
                if mini_left==mini_right and mini_left==-1:
                    return -1
                elif mini_left!=-1 and mini_right!=-1:
                    return min(mini_left, mini_right)
                else:
                    return max(mini_left, mini_right)
            else:
                return max(root.left.val, root.right.val)
        return -1
       
        
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root.left and root.right:
            if root.val==root.left.val and root.val==root.right.val:
                return self.NextBigger(root)
            elif root.val==root.left.val:
                if self.checkCh(root.left):
                    x=0
                    if root.left.left.val==root.left.right.val:
                        x=self.NextBigger(root.left)
                    else:
                        x=max(root.left.left.val, root.left.right.val)
                    return min(root.right.val, x ) if x!=-1 else root.right.val
                else:
                    return root.right.val
            elif root.val==root.right.val:
                if self.checkCh(root.right):
                    x=0
                    if root.right.left.val==root.right.right.val:
                        x=self.NextBigger(root.right)
                    else:
                        x=max(root.right.left.val, root.right.right.val)
                    return min(root.left.val, x ) if x!=-1 else root.left.val
                else:
                    return root.left.val
        return -1