from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.heapmax=[]
        self.heapmin=[]

    def addNum(self, num: int) -> None:
        if len(self.heapmax) == 0:
            heappush(self.heapmax, -num)
        elif len(self.heapmax) > len(self.heapmin):
            heappush(self.heapmax, -num)
            ele=heappop(self.heapmax)
            heappush(self.heapmin,-ele)
        elif len(self.heapmax) == len(self.heapmin):
            heappush(self.heapmin,num)
            ele=heappop(self.heapmin)
            heappush(self.heapmax,-ele)
        return

    def findMedian(self) -> float:
        if len(self.heapmax) == len(self.heapmin):
            return ((-self.heapmax[0])+self.heapmin[0])/2
        elif len(self.heapmax) > len(self.heapmin):
            return -self.heapmax[0]
        return
    

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()