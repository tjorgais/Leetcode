# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        na=0
        nb=0
        tempa=headA
        tempb=headB
        while(tempa!=None):
            tempa=tempa.next
            na+=1
        while(tempb!=None):
            tempb=tempb.next
            nb+=1
        diff=abs(na-nb)
        tempa=headA
        tempb=headB
        if diff==0:
            while(tempa!=None or tempb!=None):
                if tempa==tempb:
                    return tempa
                tempa=tempa.next
                tempb=tempb.next
        else:
            if na>nb:
                count=0
                while(count!=diff):
                    tempa=tempa.next
                    count+=1
                while(tempa!=None or tempb!=None):
                    if tempa==tempb:
                        return tempa
                    tempa=tempa.next
                    tempb=tempb.next
            else:
                count=0
                while(count!=diff):
                    tempb=tempb.next
                    count+=1
                
                while(tempa!=None or tempb!=None):
                    if tempa==tempb:
                        return tempb
                    tempa=tempa.next
                    tempb=tempb.next
        return None
                
                    
                    
        
        