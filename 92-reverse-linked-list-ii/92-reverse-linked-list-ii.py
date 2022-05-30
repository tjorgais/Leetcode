# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left ==right:
            return head
        else:
            dummy=ListNode(-600)
            dummy.next=head
            prev=dummy
            curr=head
            i=1
            while(i!=left):
                prev=prev.next
                curr=curr.next
                i+=1
            ptr1_left=prev
            curr=curr.next
            after=curr.next
            prev=prev.next
            ptr1=prev
            while(i!=right):
                i+=1
                curr.next=prev
                prev=curr
                curr=after
                after=(curr.next)if curr else None
            
            ptr1_left.next=prev
            ptr1.next=curr
        return dummy.next
    
            
        
        