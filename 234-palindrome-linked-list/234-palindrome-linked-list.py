# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n=0
        temp=head
        while(temp.next!=None):
            n+=1
            temp=temp.next
        n+=1
        temp=head
        if n==1:
            return True
        else:
            if n%2==0:
                x=n//2-1
                i=0
                output1=''
                while(i!=x):
                    output1+=str(temp.val)
                    temp=temp.next
                    i+=1
                output1+=str(temp.val)
                output1=output1[::-1]
                output2=''
                temp=temp.next
                while(temp!=None):
                    output2+=str(temp.val)
                    temp=temp.next
                if output1==output2:
                    return True
            else:
                x=n//2-1
                i=0
                output1=''
                while(i!=x):
                    output1+=str(temp.val)
                    temp=temp.next
                    i+=1
                output1+=str(temp.val)
                output1=output1[::-1]
                output2=''
                temp=temp.next.next
                while(temp!=None):
                    output2+=str(temp.val)
                    temp=temp.next
                print(output2)
                if output1==output2:
                    return True
        return False
            
            
                
            
                