# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow =head 
        fast=head
        found=False
        while slow and fast.next and (fast.next).next:
            
            slow=slow.next
            fast=(fast.next).next
            if slow == fast:
                found=True
                break


        if found==True:
            fast=head
            while fast !=slow:
                slow=slow.next 
                fast=fast.next
            return fast

        return None
            
        