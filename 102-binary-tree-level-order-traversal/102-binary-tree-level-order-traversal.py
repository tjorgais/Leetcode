# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        output=[]
        stack1=[]
        stack2=[]
        stack1.append(root)
        while True:
            level=[]
            while stack1:
                ele=stack1.pop()
                if ele is not None:
                    level.append(ele.val)
                    stack2.append(ele.right)
                    stack2.append(ele.left)
            if len(level)!=0:    
                output.append(level[::-1])
            else:
                break
            level=[]
            while stack2:
                ele=stack2.pop()
                if ele is not None:
                    level.append(ele.val)
                    stack1.append(ele.left)
                    stack1.append(ele.right)
            if len(level)!=0:   
                output.append(level)
            else:
                break
            
        return output
    
            
        