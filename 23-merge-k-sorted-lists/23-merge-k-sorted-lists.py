
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop

def add_list(head, n):
    temp=head
    if head==None:
        temp=ListNode(n)
        head=temp
        
    else:
        node=ListNode(n)
        while(temp.next!=None):
            temp=temp.next
        temp.next=node
    return head 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)
        heap=[]
        temp3=None
        if n==0:
            return None
        else:
            for temp in lists:
                while(temp!=None):
                    heapq.heappush(heap, temp.val)
                    temp=temp.next
            while(len(heap)!=0):
                ele=heapq.heappop(heap)
                temp3=add_list(temp3, ele)
            return temp3
                
            
                
                
            
        
 