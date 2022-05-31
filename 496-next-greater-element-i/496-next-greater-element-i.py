class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        func={}
        stack=[]
        n1=len(nums1)
        n2=len(nums2)
        for i in range(n2):
            if len(stack)==0 or stack[-1]>nums2[i]:
                stack.append(nums2[i])
            else:
                while(len(stack)!=0 and stack[-1]<nums2[i]):
                    func[stack.pop()]=nums2[i]
                stack.append(nums2[i])
        if len(stack)!=0:
            while(len(stack)!=0):
                func[stack.pop()]=-1
        nums2.clear()
        for i in range(n1):
            nums2.append(func[nums1[i]])
        return nums2
                
                
                    
        