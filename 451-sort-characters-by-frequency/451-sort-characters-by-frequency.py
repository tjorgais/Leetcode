class Solution:
    def frequencySort(self, s: str) -> str:
        func={}
        n=len(s)
        for i in range(n):
            if s[i] not in func:
                func[s[i]]=1
            else:
                func[s[i]]+=1
        func=dict(sorted(func.items(),reverse=True, key=lambda x:x[1]))
        st=''
        for key in func.keys():
            
            x=func[key]
            while(x):
                st+=key
                x-=1
        return st
                
        