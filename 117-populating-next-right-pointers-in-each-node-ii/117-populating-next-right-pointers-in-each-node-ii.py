"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def __init__(self):
        self.func={}
    def connectRight(self,root,row, col ):
        if root==None:
            return 
        arr=self.func.get(row,[])
        arr.append([root, col])
        self.func[row]=arr
        self.connectRight(root.left,row+1,col-1)
        self.connectRight(root.right, row+1,col+1)
        return
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root==None:
            return None
        self.connectRight(root,0,0)
        for key in sorted(self.func.keys()):
            sorted(self.func[key], key= lambda x: (x[1]))
            n=len(self.func[key])
            for i in range(n-1):
                self.func[key][i][0].next=self.func[key][i+1][0]
            self.func[key][n-1][0].next=None
        return root
            
        