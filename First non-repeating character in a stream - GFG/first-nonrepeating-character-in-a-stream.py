
class Solution:
    def firstUniqChar(self, arr):
        v=[]
        for i in range(26):
            if arr[i][0]==1:
                v.append(arr[i][1])
        if not v:
            return '#'
        else:
            return min(v)
                
	def FirstNonRepeating(self, A):
	    n=len(A)
		output=''
		arr=[[] for i in range(26)]
		for i in range(26):
		    arr[i]=[0,0]
		i=0
		while(i!=n):
		    x=ord(A[i])-97
	        arr[x][0]+=1
	        arr[x][1]=i
	        res=self.firstUniqChar(arr)
	        if res=='#':
	            output+=res
	        else:
	            output+=A[res]
	        i+=1
		return output
		
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends