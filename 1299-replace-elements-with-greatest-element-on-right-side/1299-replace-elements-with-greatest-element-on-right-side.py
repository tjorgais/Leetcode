class Solution(object):
    def replaceElements(self, arr):
        '''
        n=len(arr)
        max_ele=0
        
        for i in range(n):
            if n-i-1==n-1:
                max_ele=arr[n-i-1]
                arr[n-i-1]=-1
            else:
                
                if(arr[n-i-1]>max_ele):
                    t=max_ele
                    max_ele=arr[n-i-1]
                    arr[n-i-1]=t
                else:
                    arr[n-i-1]=max_ele
        return arr
        '''
        n=len(arr)
        max_ele=-1
        for i in range(n-1, -1, -1):
            new_max=0
            if arr[i]>max_ele:
                new_max=arr[i]
            arr[i]=max_ele
            if new_max>max_ele:
                max_ele=new_max
        return arr
            

        
                    
                
                
                
            
            
        '''           
            if i==n-1:
                arr[i]=-1
            else:
                arr[i]=max(arr[i+1:])
        
        '''
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        