from heapq import heappush, heappop
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        func=Counter(tasks)
        heap=[]
        heapq.heapify(heap)
        count=0
        for key in func.keys():
            heappush(heap,[-func[key],key])
        
        
        st=''
        while(heap):
            x, y=heappop(heap)
            
            st+=y
            x+=1
            count+=1
            
            stack=[]
            i=0
            if x!=0:
                while(i!=n):
                    if heap:
                        p,q=heappop(heap)
                        p+=1
                        st+=q
                        if p!=0:
                            stack.append([p,q])
                        count+=1
                    else:
                        #idle
                        st+='_'
                        count+=1
                    i+=1
                if stack:
                    while(stack):
                        heappush(heap, stack.pop())
                heappush(heap, [x,y])
            else:
                if heap:
                    p,q=heappop(heap)
                    count+=1
                
        print(st)
    
        return count
                    
            
                    
            
            
        
        
        