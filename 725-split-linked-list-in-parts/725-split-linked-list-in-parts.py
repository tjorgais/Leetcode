# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math 
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n=0
        temp=head
        while(temp!=None):
            temp=temp.next
            n+=1
        output=[]
        temp=head
        curr=head
        while(k):
            x=math.ceil(n/k)
            if x==0:
                output.append(None)
                k-=1
            else:
                output.append(temp)
                for i in range(x-1):
                    curr=curr.next
                temp=curr.next
                curr.next=None
                curr=temp
                n-=x
                k-=1
        return output
                
            
        return output
                    
                    
            
                
                
        