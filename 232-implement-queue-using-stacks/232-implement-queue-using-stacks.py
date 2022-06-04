class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.top1=-1
        self.stack2=[]
        self.top2=-1

    def push(self, x: int) -> None:
        if self.top1==-1:
            self.top1+=1
            self.stack1.append(x)
        else:
            while(self.top1!=-1):
                self.stack2.append(self.stack1.pop())
                self.top2+=1
                self.top1-=1
            self.stack1.append(x)
            self.top1+=1
            while(self.top2!=-1):
                self.stack1.append(self.stack2.pop())
                self.top1+=1
                self.top2-=1
            
        

    def pop(self) -> int:
        self.top1-=1
        return self.stack1.pop()
        

    def peek(self) -> int:
        return self.stack1[self.top1]
        

    def empty(self) -> bool:
        return True if self.top1==-1 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()