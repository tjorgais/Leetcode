#Your task is to complete this function
#Function should return complete string
def encode(arr):
    n=len(arr)
    i=0
    s=''
    while(True):
        count=1
        while(i<n-1 and arr[i+1]==arr[i]):
            count+=1
            i+=1
        
        s+=arr[i]+str(count)
        if i==n-1:
            break
        i+=1
        
    return s
        
    # Code here

#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends