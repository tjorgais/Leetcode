"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp=head
        temp2=None
        if head==None:
            return temp2
        else:
            
            while(temp!=None):
                temp2=Node(temp.val)
                temp2.next=temp.next
                temp.next=temp2
                temp=temp.next.next
            temp=head
            while(temp!=None):
                if temp.random:
                    temp.next.random=temp.random.next
                temp=temp.next.next
            
            temp=head

            temp2=head.next
            temp3=temp2
            while(temp.next.next!=None):
                temp.next=temp.next.next
                temp2.next=temp2.next.next
                temp=temp.next
                temp2=temp2.next
            temp.next=None
            temp2.next=None
            return temp3
                
                
                
            
        