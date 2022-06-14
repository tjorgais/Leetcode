# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def checkleft(parent, root):
#     if root==None:
#         return True
#     if root.val<parent.val:
#         return (checkleft(root, root.left) and checkright(root, root.right))
#     return False
# def checkright(parent, root):
#     if root==None:
#         return True
#     if root.val>parent.val:
#         return (checkleft(root, root.left) and checkright(root, root.right))
#     return False
    
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if root==None:
#             return True

#         return (checkleft(root, root.left) and checkright(root, root.right))

def inorder(root, output):
    if root== None:
        return output
    output=inorder(root.left, output)
    output.append(root.val)
    output=inorder(root.right, output)
    
    return output
    
class Solution:
       def isValidBST(self, root: Optional[TreeNode]) -> bool:
            output=[]
            output=inorder(root, output)
            if len(output)==1:
                return True
            for i in range(len(output)-1):
                if output[i+1]<=output[i]:
                    return False
            return True
                
            
        
        