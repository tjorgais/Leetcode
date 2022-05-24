# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        temp=head
        while(temp!=None):
            temp=temp.next
            count+=1
        temp=head
        if count==1:
            return head
        else:
            i=0
            temp2=head
            while(i!=k-1):
                temp2=temp2.next
                i+=1
            j=0
            while(j!=count-k):

                temp=temp.next
                j+=1
            temp.val, temp2.val=temp2.val, temp.val
            return head
                
        