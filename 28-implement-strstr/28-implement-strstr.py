class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n1=len(haystack)
        n2=len(needle)
        if n1<n2:
            return -1
        func={}
        for i in range(26):
            func[chr(97+i)]=i+1
        
        hash=0
        x=0
        start=0
        for i in range(n2):
            
            hash+=func[needle[i]]*pow(10,n2-i-1)
            x+=func[haystack[i]]*pow(10,n2-i-1)
        
        if hash==x:
            
            
            for j in range(n2):
                
                if haystack[start+j]!=needle[j]:
                    break
                if j==n2-1:
                    return start
        
        for i in range(n2, n1):
            
            x-=func[haystack[start]]*pow(10,n2-1)
            x=x*10+func[haystack[i]]
            start+=1
            
            if x==hash:
                for j in range(n2):
                    if haystack[start+j]!=needle[j]:
                        break
                if j==n2-1:
                    return start
            
        return -1
            
        
        
        
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
        