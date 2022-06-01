class MinStack:

    def __init__(self):
        self.stack=[]
    def push(self, val: int) -> None:
        #lst = list()
        self.stack.append(val)
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)




# class MinStack:

#     def __init__(self):
#         self.stack=[]
#         self.min_stack=[]
#         self.min=float('inf')
        

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if len(self.stack)==0:
#             self.min_stack.append(val)
#             self.min=val
#         else:
#             if val>=self.min: 
#                 self.min_stack.append(val)
#             else:
#                 self.min_stack.append(2*val-self.min)
#                 self.min=val
        

#     def pop(self) -> None:
#         self.stack.pop()
#         if self.min_stack[-1]<self.min:
#             self.min=2*self.min-self.min_stack[-1]
#             self.min_stack.pop()
#         else:
#             self.min_stack.pop()
            
#     def top(self) -> int:
#         return self.stack[-1]
        

#     def getMin(self) -> int:
#         return self.min
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()