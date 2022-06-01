
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        func={}
        stack=[]
        for i in range(n):
            if len(stack)==0 or stack[-1][0]>nums[i]:
                stack.append((nums[i],i))
            else:
                while(len(stack)!=0 and stack[-1][0]<nums[i]):
                    func[stack.pop()]=nums[i]
                stack.append((nums[i],i))
        if len(stack)!=0:
            for i in range(n-1):
                if len(stack)==0:
                    break
                else:
                    while(len(stack)!=0 and stack[-1][0]<nums[i]):
                        func[stack.pop()]=nums[i]
        if len(stack)!=0:
            while(len(stack)!=0):
                func[stack.pop()]=-1
        
        for i in range(n):
            nums[i]=func[(nums[i],i)] #Using the same memory
        return nums
            
        


        