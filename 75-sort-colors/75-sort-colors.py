class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N=len(nums)
        i=0
        j=N-1
        while(i<j):
            
            if(nums[j]==0):
                nums[i],nums[j]=nums[j],nums[i]
                i=i+1
            elif (nums[j]==2):
                j=j-1
            else:
                if(nums[i]==0):
                    i=i+1
                elif(nums[i]==2):
                    
                    nums[i],nums[j]=nums[j],nums[i]
                    j=j-1
                else:
                    
                    k=j-1
                    while(i<k):
                        if(nums[k]==1):
                            k=k-1
                        elif (nums[k]==0):
                            nums[i],nums[k]=nums[k],nums[i]
                            break
                        else:
                            nums[i],nums[k]=nums[k],nums[i]
                            break
                    
                    if(i==k):
                        j=k
                        
                            
                            


