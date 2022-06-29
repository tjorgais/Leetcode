# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.func={}
        
    def Mode(self, root):
        if root==None:
            return 
        if root.val not in self.func:
            self.func[root.val]=1
        else:
            self.func[root.val]+=1
        self.Mode(root.left)
        self.Mode(root.right)
        return
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return 
        self.Mode(root)
        output=[]
        i=0
        inital=0
        for key in sorted(self.func.items(), reverse=True, key=lambda x: x[1]):
            if i!=0:
                if key[1]==inital:
                    output.append(key[0])
                else:
                    break
            else:
                output.append(key[0])
                inital=key[1]
            i+=1
        return output
                
            
        # output=[]
        # for key in self.func.keys():
        #     output.append(self.func[key])
        
    