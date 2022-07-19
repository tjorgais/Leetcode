class Solution:
    def generate_lps(self, needle, lps, m):
        len=0
        i=1
        while i<m:
            if needle[i]==needle[len]:
                len+=1
                lps[i]=len
                i+=1
            else:
                if len!=0:
                   len=lps[len-1]
                else:
                    lps[i]=0
                    i+=1
                
        
    def strStr(self, haystack: str, needle: str) -> int:
        #KMP Algorithm
        n=len(haystack)
        m=len(needle)
        lps=[0]*m
        self.generate_lps(needle, lps, m)
        i,j=0,0
        while i<n:
            
            if haystack[i]==needle[j]:
                j=j+1
                i+=1
                if j==m:
                    return i-j
            else:
                if j!=0:
                    
                    j=lps[j-1]
                else:
                    i+=1
        return -1
        
        
        
        
        
        
        
        # Robin Karp Algorithm O(m*n) in worse case
        
#         n1=len(haystack)
#         n2=len(needle)
#         if n1<n2:
#             return -1
#         func={}
#         for i in range(26):
#             func[chr(97+i)]=i+1
        
#         hash=0
#         x=0
#         start=0
#         for i in range(n2):
            
#             hash+=func[needle[i]]*pow(10,n2-i-1)
#             x+=func[haystack[i]]*pow(10,n2-i-1)
        
#         if hash==x:
            
            
#             for j in range(n2):
                
#                 if haystack[start+j]!=needle[j]:
#                     break
#                 if j==n2-1:
#                     return start
        
#         for i in range(n2, n1):
            
#             x-=func[haystack[start]]*pow(10,n2-1)
#             x=x*10+func[haystack[i]]
#             start+=1
            
#             if x==hash:
#                 for j in range(n2):
#                     if haystack[start+j]!=needle[j]:
#                         break
#                 if j==n2-1:
#                     return start
            
#         return -1
            
        
        
        
        # n1=len(haystack)
        # n2=len(needle)
        # if n1<n2:
        #     return -1
        # elif n2==0:
        #     return 0
        # else:
        #     for i in range(n1-n2+1):
        #         for j in range(n2):
        #             if haystack[i+j]!=needle[j]:
        #                 break
        #             if j==n2-1:
        #                 return i
        #     return -1
        