class Solution(object):
    def findUnsortedSubarray(self, nums):
        
        n=len(nums)
        start=n-1
        end=0
        nums2=list(nums)
        nums2=sorted(nums2)
        for i in range(n):
            if(nums[i]!=nums2[i]):
                start=min(start,i)
            if(nums[n-i-1]!=nums2[n-i-1]):
                end=max(end,n-i-1)
        if start>=end:
            return 0
        else:
            return end-start+1
        
        #Method1 (It gives runtime error)
        '''
        n=len(nums)
        start=n-1
        end=0
        for i in range(n):
            for j in range(i,n):
                if(nums[i]>nums[j]):
                    start=min(start,i)
                    end=max(end,j)
        if start>=end:
            return 0
        else :
            return end-start+1
        
        '''
        