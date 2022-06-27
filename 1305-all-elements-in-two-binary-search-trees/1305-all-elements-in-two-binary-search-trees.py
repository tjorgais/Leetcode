# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

        
    def inorder(self, root,list1):
        if root==None:
            return list1
        list1=self.inorder(root.left,list1)
        list1.append(root.val)
        list1=self.inorder(root.right,list1)
        return list1
            
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1=[]
        list2=[]
        output=[]
        list1=self.inorder(root1,list1)
        list2=self.inorder(root2, list2)
        # print(list1)
        # print(list2)
        n1=len(list1)
        n2=len(list2)
        i,j=0,0
        while(i!=n1 and j!=n2):
            #print(i,j)
            if list1[i]<list2[j]:
                output.append(list1[i])
                i+=1
            else:
                output.append(list2[j])
                j+=1
        if i!=n1:
            while(i!=n1):
                output.append(list1[i])
                i+=1
        else:
            while(j!=n2):
                output.append(list2[j])
                j+=1
        return output
            
        