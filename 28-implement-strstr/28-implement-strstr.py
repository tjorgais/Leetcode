class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1=len(haystack)
        n2=len(needle)
        if n1<n2:
            return -1
        elif n2==0:
            return 0
        else:
            for i in range(n1-n2+1):
                for j in range(n2):
                    if haystack[i+j]!=needle[j]:
                        break
                    if j==n2-1:
                        return i
            return -1
        