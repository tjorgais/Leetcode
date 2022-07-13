from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1=len(s)
        n2=len(p)
        if n2>n1:
            return None

        
        func2=Counter(p)
        i=0
        j=n2
        func1=Counter(s[:j])
        output=[]
        
        for i in range(j,n1):
            
            if func1==func2:
                output.append(i-n2)
            func1[s[i]]+=1
            func1[s[i-n2]]-=1
        
        if func2==func1:
            output.append(n1-n2)
            
        return output
        