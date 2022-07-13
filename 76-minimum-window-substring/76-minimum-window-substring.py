import sys
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1=len(s)
        n2=len(t)
        ans=''
        if n2>n1:
            return ans
        func1={}
        func2={}
        for i in range(n2):
            if t[i] in func2:
                func2[t[i]]+=1
            else:
                func2[t[i]]=1
                func1[t[i]]=0
        i=0
        j=0
        output=[]
        start_ind=-1
        minlen=n1+100
        count=0
        start=0
        for i in range(n1):
            c=s[i]
            if c in func1:
                func1[c]+=1
                if func1[c]<=func2[c]:
                    count+=1
                if count==n2:
                    while s[start] not in func2 or func1[s[start]]>func2[s[start]]:
                        if s[start] in func2:
                            if func1[s[start]]>func2[s[start]]:
                                func1[s[start]]-=1
                            
                        start+=1
                    winlen=i-start+1
                    if winlen<minlen:
                        minlen=winlen
                        start_ind=start
        if start_ind==-1:
            return ""
        return s[start_ind: start_ind+minlen]
                        

                    
                    
                    
            
        
        
        
#         while(j<n1):
#             if s[j] in func1:
#                 func[s[j]]+=1
#             else:
#                 func1[s[j]]=1
#             for key in func2.keys():
#                 if func1[key]==fun2[key]:
#                     continue
#                 elif func1[key]<func2[key]:
#                     j+=1
#                     break
#                 else:
#                     while(func1[key]!=func2[key])
#                         func1[s[i]]-=1
#                         i+=1
                    
#             ans+=s[i:j+1]
#         return ans
        
                    
            