from collections import Counter, defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n=len(s)
        func1={}
        func2=Counter(words)
        m=len(words[0])
        win=m*len(words)
        if n<win:
            return None
        start=0
        output=[]
        i=start
        j=start+m

        while(i+win<=n):
            func1={}
            while(i!=start+win):
                if s[i:j] in func1:
                    func1[s[i:j]]+=1
                else:
                    func1[s[i:j]]=1      
                i=j
                j+=m

            if func1==func2:
                output.append(start)
            start+=1
            i=start
            j=start+m
        return output
            
            
            
                
        
            
            
            
        
        