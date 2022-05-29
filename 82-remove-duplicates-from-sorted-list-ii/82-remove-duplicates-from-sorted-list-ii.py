# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        while(curr!=None):
            while(curr.next!=None and prev.next.val==curr.next.val):
                curr=curr.next
            if prev.next==curr:
                prev=curr
            else:
                prev.next=curr.next
            curr=curr.next
        return dummy.next
                

        