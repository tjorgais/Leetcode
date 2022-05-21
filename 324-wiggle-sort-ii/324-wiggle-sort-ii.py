class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n=len(nums)
        nums.sort()
        arr=[nums[i] for i in range(n)]
        j=n-1
        i=1
        while(i<n):
            nums[i]=arr[j]
            j-=1
            i+=2
        i=0
        while(i<n):
            nums[i]=arr[j]
            j-=1
            i+=2



        return nums

