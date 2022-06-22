# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def vertical(self,root, row, col):
        if root==None:
            return
        arr=self.func.get(col,[])
        arr.append([root, row])
        self.func[col]=arr
        self.vertical(root.left,row+1,col-1)
        self.vertical(root.right, row+1, col+1)
        return 
            
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.func={}
        self.vertical(root,0,0)
        result=[]
        for key in sorted(self.func.keys()):
            result.append([])
            for y in sorted(self.func[key], key= lambda x: (x[1], x[0].val)):
                result[-1].append(y[0].val)
        return result
        