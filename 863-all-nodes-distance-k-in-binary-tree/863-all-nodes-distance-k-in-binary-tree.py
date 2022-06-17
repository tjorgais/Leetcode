# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def FindKdistdown(root, k,output):
    if root==None:
        return output
    if k==0:
        output.append(root.val)
        return output
    output=FindKdistdown(root.left,k-1,output)
    output=FindKdistdown(root.right,k-1,output)
    return output

def Kdistance(root,target, k,output):
    if root==None:
        return output,-1
    if root==target:
        output=FindKdistdown(root,k,output)
        return output,0
    output,dl=Kdistance(root.left, target, k,output)
    if dl!=-1:
        if dl+1==k:
            output.append(root.val)
        else:
            output=FindKdistdown(root.right,k-dl-2,output)
        return output,dl+1
    output, dr = Kdistance(root.right, target, k,output)
    if dr!=-1:
        if dr+1==k:
            output.append(root.val)
        else:
            output=FindKdistdown(root.left,k-dr-2,output)
        return output,dr+1
    return output, -1
        
    

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        output=[]
        output,dist=Kdistance(root,target, k, output)
        return output

        
            
            
        