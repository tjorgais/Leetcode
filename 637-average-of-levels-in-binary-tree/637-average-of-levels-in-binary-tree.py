# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        output=[]
        stack1=[]
        stack2=[]
        stack1.append(root)
        while True:
            count=0
            x=0
            while stack1:
                
                ele=stack1.pop()
                if ele is not None:
                    x+=ele.val
                    count+=1
                    stack2.append(ele.right)
                    stack2.append(ele.left)
            if count!=0:    
                output.append(x/count)
            else:
                break
            count=0
            x=0
            while stack2:
                ele=stack2.pop()
                if ele is not None:
                    count+=1
                    x+=ele.val
                    stack1.append(ele.left)
                    stack1.append(ele.right)
            if count!=0:   
                output.append(x/count)
            else:
                break
            
        return output
    