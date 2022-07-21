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
    def longestPrefix(self, s: str) -> str:
        n=len(s)
        lps=[0]*n
        self.generate_lps(s,lps, n)
        
        return s[:lps[-1]]
        
        