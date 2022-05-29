# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        elif head.next==None:
            return head
        else:
            odd=head
            even=head.next
            ptr=even
            n=0
            while(odd!=None):
                odd=odd.next
                n+=1
            odd=head    
            if n%2==0:
                while(odd.next.next!=None):
                    odd.next=odd.next.next
                    even.next=even.next.next
                    odd=odd.next
                    even=even.next
                
                odd.next=ptr
                return head
                
            else:
                while(even.next.next!=None):
                    odd.next=odd.next.next
                    even.next=even.next.next
                    odd=odd.next
                    even=even.next
                odd.next=odd.next.next
                odd=odd.next
                even.next=None
                odd.next=ptr
                return head
                
        return