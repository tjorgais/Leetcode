class Solution(object):
    def findDuplicates(self, nums):
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return [i for i,j in d.items() if j==2]
                
            
              
        

        