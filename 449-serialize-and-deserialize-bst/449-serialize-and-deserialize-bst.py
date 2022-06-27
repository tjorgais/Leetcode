# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def inorder(self,root, output):
        x=root.val
        if x<0:
            x='n'+str(x)[1:]
        else:
            x=str(x)
        if root.left==None and root.right==None:
            output=output+x+"#" #-leaf node
            
        elif root.left==None:
            output+=x+"/"   #'/'-left null
            output=self.inorder(root.right,output)
        elif root.right==None:
            output=output+x+"\\"
            output=self.inorder(root.left,output)
            
        else:
            output+=x+"*"     #*-internal node
            output=self.inorder(root.left,output)
            output=self.inorder(root.right, output)
            
        return output

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        output=''
        if root==None:
            return output
        output=self.inorder(root, output)
        #print(output)
        return output
    
    def reconstruct(self):
        if self.data=='':
            return 
        num=''
        root=None
        x=self.data[0]
        if x=='n':
            num+='-'
            self.data=self.data[1:]
            x=self.data[0]
        while(x.isnumeric()):
            num+=x
            self.data=self.data[1:]
            x=self.data[0]
        self.data=self.data[1:]
        #print(num)
        num=int(num)
        
        if x=='*':
            root=TreeNode(num)
            root.left =self.reconstruct()
            root.right=self.reconstruct()
        elif x=="/":
            root=TreeNode(num)
            root.left=None
            root.right=self.reconstruct()
        elif x=="\\":
            root=TreeNode(num)
            root.left=self.reconstruct()
            root.right=None
        else:
            root=TreeNode(num)
            root.left=None
            root.right=None
        return root

        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data=='':
            return None
        self.data=data
        root=self.reconstruct()
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans