# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_k_group(head, k):
    prev=None
    after=None
    curr=head
    n=0
    while(curr!=None):
        curr=curr.next
        n+=1

    curr=head
    if n<k:
        return head
    else:
        i=0
        while(i!=k and curr!=None):
            after=curr.next
            curr.next=prev
            prev=curr
            curr=after
            i+=1


        head.next=reverse_k_group(curr,k)
        head=prev
        return head

    
    
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return reverse_k_group(head, k)


                    
                
                    
            
                    
                
            
        
        