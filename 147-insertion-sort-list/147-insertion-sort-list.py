# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseLLUsingStack( head):
    stack, temp = [], head

    while temp:
        stack.append(temp)
        temp = temp.next

    head = temp = stack.pop()

    while len(stack) > 0:
        temp.next = stack.pop()
        temp = temp.next

    temp.next = None
    return head

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        insertion=head
        if insertion==None:
            return insertion
        head=head.next
        insertion.next=None

        while(head!=None):
            ptr=head
            prev=None
            temp=insertion
            move=False
            while(temp!=None and ptr.val<=temp.val):

                prev=temp
                temp=temp.next
                move=True
            if move==True:
                prev.next=ptr
                head=ptr.next
                if temp==None:
                    ptr.next=None
                else:
                    ptr.next=temp
            else:
                insertion=ptr
                prev=insertion
                head=ptr.next
                if temp==None:
                    ptr.next=None
                else:
                    ptr.next=temp
        
        insertion=reverseLLUsingStack(insertion)
        return insertion

            
        