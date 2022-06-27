# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output=[]
        self.func={}
    def rightview(self,root, row, col):
        if root==None:
            return None
        arr=self.func.get(row,[])
        arr.append([root, col])
        self.func[row]=arr
        self.rightview(root.left, row+1, col-1)
        self.rightview(root.right, row+1,col+1)
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return None
        self.rightview(root,0,0)
        for key in sorted(self.func.keys()):
            sorted(self.func[key], key= lambda x: x[1])
            #print(self.func[key][-1])
            self.output.append(self.func[key][-1][0].val)
            
        
        return self.output
        