#User function Template for python3

'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def splitList(self, head, head1, head2):
        #code here
        n=0
        temp=head
        while(temp.next!=head):
            n+=1
            temp=temp.next
        n+=1
        temp=head
        ptr1=None
        ptr2=None
        if n%2==0:
            head1=head
            i=0
            while(i!=(n//2)-1):
                temp=temp.next
                i+=1
            ptr1=temp
            head2=temp.next
            while(temp.next!=head):
                temp=temp.next
            ptr2=temp
            ptr1.next=head1
            ptr2.next=head2
        else:
            head1=head
            i=0
            while(i!=(n//2)):
                temp=temp.next
                i+=1
            ptr1=temp
            head2=temp.next
            while(temp.next!=head):
                temp=temp.next
            ptr2=temp
            ptr1.next=head1
            ptr2.next=head2
                
        
        
        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2

#{ 
#  Driver Code Starts
#Initial Template for Python 3


class Node:
    def __init__(self):
        self.data = None
        self.next = None

def printCircularLinkedList(head):
    tmp = head
    while True:
        print(tmp.data, end = " ")
        tmp = tmp.next
        if tmp == head:
            break
    print()
    
if __name__ == "__main__":
    for i in range(int(input())):
        head = Node()
        head1 = Node()
        head2 = Node()
        tmp = head
        n = int(input())
        for i in input().split():
            tmp.next = Node()
            tmp = tmp.next
            tmp.data = int(i)
        head = head.next
        tmp.next = head
        obj = Solution()
        head1,head2 = obj.splitList(head,head1,head2)
        printCircularLinkedList(head1)
        printCircularLinkedList(head2)


# } Driver Code Ends