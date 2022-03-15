class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        N=len(nums)
        found=False
        
        for i in range(N):
            
            next_greater=False
            mini=nums[i]
            for j in range(i+1,N):
                if nums[j]>nums[i] and next_greater:
                    if nums[j]>mini:
                        found=True
                        break
                    else:
                        mini=nums[j]
                elif nums[j]>nums[i]:
                    mini=nums[j]
                    next_greater=True
                else:
                    continue
            if(found):
                break
        return found
        '''
        N=len(nums)
        mini_ind=0
        low=-1
        mid=-1
        x=set(nums)
        if len(x)<3:
            
            return False
        else:
            for i in range(0,N):
                if(nums[i]<=nums[mini_ind]):
                    mini_ind=i
                elif(nums[i]>nums[mini_ind] and low==-1 ):
                    low=mini_ind
                    mid=i
                elif(nums[i]<=nums[mid]):
                    low=mini_ind
                    mid=i
                else:
                    print(i)
                    return True
        return False
                
            
                    
                
                    
                    
                
        