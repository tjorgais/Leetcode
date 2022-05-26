# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp3=None
        temp1=l1
        temp2=l2
        carry=0
        have_carry=False
        while(temp1!=None and temp2!=None):
            if have_carry:
                x=temp1.val+temp2.val+carry
                have_carry=False
                carry=0
            else:
                x=temp1.val+temp2.val
            if x>9:
                y=x%10
                z=(int)(x//10)
                temp3=add_list(temp3, y)
                carry=z
                have_carry=True
            else:
                temp3=add_list(temp3, x)
            temp1=temp1.next
            temp2=temp2.next
        if temp1!=None:
            while(temp1!=None):
                if have_carry:
                    x=temp1.val+carry
                    have_carry=False
                    carry=0
                else:
                    x=temp1.val
                if x>9:
                    y=x%10
                    z=(int)(x//10)
                    temp3=add_list(temp3, y)
                    carry=z
                    have_carry=True
                else:
                    temp3=add_list(temp3, x)
                temp1=temp1.next
        if temp2!=None:
            while(temp2!=None):
                if have_carry:
                    x=temp2.val+carry
                    have_carry=False
                    carry=0
                else:
                    x=temp2.val
                if x>9:
                    y=x%10
                    z=(int)(x//10)
                    temp3=add_list(temp3, y)
                    carry=z
                    have_carry=True
                else:
                    temp3=add_list(temp3, x)
                temp2=temp2.next
        if have_carry==True:
            temp3=add_list(temp3, carry)
        return temp3
                
                
        