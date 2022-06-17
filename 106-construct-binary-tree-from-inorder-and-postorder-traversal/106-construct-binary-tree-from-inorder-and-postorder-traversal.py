# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        root=None
        #print(inorder)
        #print(postorder)
        if n==0:
            return None
        if n==1:
            root=TreeNode(postorder.pop())
            return root
        
        ele=postorder.pop()
        i=0
        for i in range(0,n):
            if ele==inorder[i]:
                root=TreeNode(ele)
                break
        
        m=len(inorder[:i])
        
        
        root.left=self.buildTree(inorder[:i], postorder[:m])
        root.right=self.buildTree(inorder[i+1:],postorder[m:])

            
       
        return root
                    
            
            
        