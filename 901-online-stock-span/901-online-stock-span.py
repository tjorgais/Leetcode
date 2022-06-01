class StockSpanner:

    def __init__(self):
        self.stack=[]
        self.count=-1

    def next(self, price: int) -> int:
        self.count+=1
        output=0
        while len(self.stack)!=0 and self.stack[-1][0]<=price:
            self.stack.pop()
        if len(self.stack)==0:
            output=self.count+1
        else:
            output=self.count - self.stack[-1][1]
        self.stack.append([price, self.count])
        return output

        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)