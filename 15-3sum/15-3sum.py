class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        my_list=[]


        for i in range(n-2):

            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while(j<k):
                x=nums[i]+nums[j]+nums[k]

                if x>0:
                    k=k-1
                elif x<0:
                    j=j+1
                else:
                    my_list.append((nums[i], nums[j], nums[k]))

                    k=k-1
                    while j<k and nums[k]==nums[k+1]:
                        k=k-1

        return my_list
