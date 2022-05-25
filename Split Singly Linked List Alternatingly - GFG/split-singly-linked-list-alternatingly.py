#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

'''
These are global variables to store heads of split lists
a --- store head of first list
b --- store head of second list
'''
def join_to_a(head, a):
    temp=head
    temp2=a
    if head.next==None:
        head=None
        if a==None:
            a=temp
            
        else:
            temp.next=a
            a=temp
            
    else:
        head=temp.next
        if a==None:
            a=temp
            a.next=None
        else:
            temp.next=a
            a=temp
            
    return head, a

            
        
        

def alternatingSplitList(head):
    global a,b
    a=None
    b=None
    if head.next==None:
        a=head
        return a, b
    else:
        temp=head
        while(temp!=None and temp.next!=None):
            temp,a=join_to_a(temp, a)
            temp,b=join_to_a(temp,b )
        if temp!=None:
            temp, a=join_to_a(temp,a)
    return
            
            
        
    
    #Your code here

#{ 
#  Driver Code Starts

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    temp = head
    while (temp):
        print(temp.data, end=" ")
        
        temp = temp.next
    print()

a=None
b=None
def append(head,data): 
  
    new_node = Node(data)
    if head is None:
        head=new_node
    else:
        new_node.next=head
        head=new_node
    
    return head
    



if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        
        head=None
        a=None
        b=None
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in (values):
            head=append(head,i)
        alternatingSplitList(head)
         
        if n%2 is 0:
            a,b=b,a #Correcting the nodes
        printList(a)
        printList(b)
        t -= 1

# } Driver Code Ends