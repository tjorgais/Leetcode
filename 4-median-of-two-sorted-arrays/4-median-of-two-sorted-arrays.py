class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2=len(nums2)

        i=0
        j=0
        result=[]
        while(i<n1 and j<n2):
            if nums1[i]<=nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        if i<n1:
            while(i<n1):
                result.append(nums1[i])
                i+=1
        if j<n2:
            while(j<n2):
                result.append(nums2[j])
                j+=1
        x=len(result)
        if x%2==0:
            return (result[x//2]+result[x//2-1])/2
        else:
            return result[x//2]




        return