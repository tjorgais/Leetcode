class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        end=1
        n=len(gas)
        if n==1:
            if gas[0]-cost[0]<0:
                return -1
            else:
                return 0
        else:
            curr_petrol=gas[start]-cost[start]
            while end!=start or curr_petrol<0:
                while curr_petrol<0 and start!=end:
                    curr_petrol=curr_petrol-(gas[start]-cost[start])
                    start=(start+1)%n
                    if start==0:
                        return -1
                curr_petrol=curr_petrol+gas[end]-cost[end]
                end=(end+1)%n
            return start
        
        
        
#         n=len(gas)
#         sum1=sum(gas)
#         sum2=sum(cost)
#         if sum1<sum2:
#             return -1
#         else:
#             for i in range(n):
#                 gas[i]=gas[i]-cost[i]
#             for i in range(n):
#                 if gas[i]<0:
#                     continue
#                 else:
#                     reserve=gas[i]
#                     count=i+1
#                     while (count)%n!=i and reserve+gas[count%n]>=0:
#                         reserve=reserve+gas[count%n]
#                         count+=1
#                     if count%n==i:
#                         return i            
#             return -1
            
                    
        
        