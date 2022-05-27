# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        if list2==None:
            return list1
        merge=None
        if list1.val<=list2.val:
            merge=list1
            list1=list1.next
        else:
            merge=list2
            list2=list2.next
        temp=merge
        while(list1 and list2):
            if list1.val<=list2.val:
                temp.next=list1
                list1=list1.next
                temp=temp.next
            else:
                temp.next=list2
                list2=list2.next
                temp=temp.next
        if list1!=None:
            while(list1!=None):
                temp.next=list1
                list1=list1.next
                temp=temp.next
        if list2!=None:
            while(list2!=None):
                temp.next=list2
                list2=list2.next
                temp=temp.next
        return merge
        