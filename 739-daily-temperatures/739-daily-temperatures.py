class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n=len(temp)
        count=-1
        temp.reverse()
        stack=[]
        arr=[]
        for i in range(n):
            count+=1
            while len(stack)!=0 and temp[stack[-1]]<=temp[i]:
                stack.pop()
            if len(stack)==0:
                arr.append(0)
            else:
                arr.append(count - stack[-1])
            stack.append(count)
        arr.reverse()
        return arr
                                        
                                              
                                             
        

        