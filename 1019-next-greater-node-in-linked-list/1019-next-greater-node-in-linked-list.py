# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def rev(head):
  
    pre = None;
    curr = head;
    nex = curr.next;

    while (curr):
        curr.next = pre;
        pre = curr;
        curr = nex;
        nex = (curr.next) if curr else None
     
    head = pre
    return head
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if head==None:
            return None
        res=[]
        head=rev(head)
        stack=[]
        while(head):
            if len(stack)==0:
                res.append(0)
                stack.append(head.val)
            else:
                while(len(stack)!=0 and stack[-1]<=head.val):
                    stack.pop()
                if len(stack)==0:
                    res.append(0)
                    stack.append(head.val)
                else:
                    res.append(stack[-1])
                    stack.append(head.val)
            
            head=head.next
        res.reverse()
        
        return res
        
                    
        
        