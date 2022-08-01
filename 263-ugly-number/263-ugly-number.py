class Solution:
    def isUgly(self, n: int) -> bool:
        #O(nlogn) time complexity exist with similar logic using heap but can improve using arr to O(n). 
        
        arr=[1]
        p2,p3,p5=0,0,0
        x=1
        
        while(x<n):
            x=min(arr[p2]*2, arr[p3]*3, arr[p5]*5)
            arr.append(x)
            if x==arr[p2]*2:
                p2+=1
            if x==arr[p3]*3:
                p3+=1
            if x==arr[p5]*5:
                p5+=1
        #print(arr)
        
        return True if n in arr else False
                
        
        
        
        
        