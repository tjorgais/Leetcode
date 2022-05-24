# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        temp=head
        while(temp!=None):
            temp=temp.next
            count+=1
        temp=head
        if count==1:
            head=None
            return head
        elif count==n:
            head=head.next
            temp=None
            return head
        else:
            i=0
            while(i!=count-n-1):
                temp=temp.next
                i+=1
            temp.next=temp.next.next
            return head
            