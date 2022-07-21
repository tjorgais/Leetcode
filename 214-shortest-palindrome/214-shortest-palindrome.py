class Solution:
    def generate_lps(self, needle, lps, m):
        len=0
        i=1
        max_len=0
        while i<m:
            if needle[i]==needle[len]:
                len+=1
                lps[i]=len
                max_len=max(i+1, max_len)
                i+=1
            else:
                if len!=0:
                   len=lps[len-1]
                else:
                    lps[i]=0
                    i+=1
        
    def shortestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return s
        st=s+'#'+s[::-1]
        
        lps=[0]*len(st)
        self.generate_lps(st, lps, len(st) )
        return s[lps[-1]:][::-1]+s
        
            
        