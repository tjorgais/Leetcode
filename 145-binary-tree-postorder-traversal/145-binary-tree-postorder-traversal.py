# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return 
        
        recursivestack=[]
        result=[]
        recursivestack.append(root)
        while recursivestack:
            current=recursivestack.pop()
            result.append(current.val)
            if current.left:
                recursivestack.append(current.left)
            if current.right:
                recursivestack.append(current.right)

        result.reverse() 
        return result
            
        