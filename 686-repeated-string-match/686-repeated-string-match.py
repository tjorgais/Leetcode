import math
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
                
        
    def strStr(self, haystack, needle):
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
                    #print('found at i-j')
                    # j=lps[j-1]
                    return True
                
            else:
                if j!=0:
                    
                    j=lps[j-1]
                else:
                    i+=1
        return False
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n=len(a)
        m=len(b)
        if n>m:
            if self.strStr(a, b):
                return 1
            else:
                new_a=a+a
                if self.strStr(new_a, b):
                    return 2
                
        else:
            k=math.ceil(m/n)
            i=k
            st=''
            while(i!=k+2):
                st=''+i*(a)
                # print(st)
                # print(b)
                if self.strStr(st,b):
                    return i
                i+=1
        return -1
      
                    
            
        