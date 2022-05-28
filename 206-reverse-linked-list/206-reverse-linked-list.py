# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        stack=[]
        temp=head
        while(temp):
            stack.append(temp)
            temp=temp.next
        temp=head=stack.pop()
        while(len(stack)):
            temp.next=stack.pop()
            temp=temp.next
        temp.next=None
        return head
            
        
        