class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        my_set=set()


        for i in range(n-2):
            j=i+1
            k=n-1
            while(j<k):
                x=nums[i]+nums[j]+nums[k]

                if x>0:
                    k=k-1
                elif x<0:
                    j=j+1
                else:
                    my_set.add((nums[i], nums[j], nums[k]))
                    j=j+1
                    k=k-1
        m=len(my_set)
        nums.clear()
        for item in my_set:

            nums.append(list(item))




        return nums
