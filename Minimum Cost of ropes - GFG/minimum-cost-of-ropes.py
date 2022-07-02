#User function Template for python3
from heapq import heappush, heappop
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    
    def minCost(self,arr,n):
        if n==1:
            return 0
        heapq.heapify(arr)
        # print(arr)
        sum=0
        while(n!=1):
            
            val1=heappop(arr)
            val2=heappop(arr)
            heappush(arr, val1+val2)
            sum+=val1+val2
            n=len(arr)
        return sum
            
        
    
    
    # def heapify(self, arr, i, n):
        
    #     smallest=i
    #     left=2*i+1
    #     right=2*i+2
    #     if left<n and arr[left]<arr[smallest]:
    #         smallest=left
    #     if right<n and arr[right]<arr[smallest]:
    #         smallest=right
    #     if smallest!=i:
    #         arr[i], arr[smallest]=arr[smallest],arr[i]
    #         arr=self.heapify(arr, smallest, n)
    #     return arr
    # def builtheap(self, arr, n):
    #     for i in range((n//2)-1,-1,-1):
    #         arr=self.heapify(arr,i,n)
    #     return arr
    # def minCost(self,arr,n):
    #     if n==1:
    #         return 0
    #     arr=self.builtheap(arr, n)
    #     # print(arr)
    #     sum=0
    #     while(n!=1):
    #         arr[0],arr[n-1]=arr[n-1],arr[0]
    #         val1=arr[n-1]
    #         arr=arr[:n-1]
    #         n=len(arr)
    #         arr=self.heapify(arr, 0, n)
    #         arr[0],arr[n-1]=arr[n-1],arr[0]
    #         val2=arr[n-1]
    #         arr[n-1]=val1+val2
    #         arr[0],arr[n-1]=arr[n-1],arr[0]
    #         arr=self.heapify(arr,0,n)
    #         # print(val1+val2)
    #         sum+=val1+val2
    #     return sum
            
            
        
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict
# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minCost(a,n))
# } Driver Code Ends