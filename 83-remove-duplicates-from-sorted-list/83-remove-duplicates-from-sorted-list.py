# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


    
    

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        else:
            prev=head
            curr=head.next
            while(curr!=None and prev!=None):
                if prev.val==curr.val:
                    prev.next=curr.next
                    curr=prev.next
                else:
                    curr=curr.next
                    prev=prev.next
            return head
        