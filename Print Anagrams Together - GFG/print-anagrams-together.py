#User function Template for python3

class Solution:
    def Anagrams(self,words, n):
        func={}
        for word in words:
            
            x=''.join(sorted(word))
            arr=func.get(x,[])
            arr.append(word)
            func[x]=arr
        output=[]
        for key in func.keys():
            output.append((func[key]))
        return output
        
            
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends