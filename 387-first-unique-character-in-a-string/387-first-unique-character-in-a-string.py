class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        func={}
        for i in range(n):
            if s[i] not in func:
                func[s[i]]=i
            else:
                func[s[i]]=-1
        mylist=[]
        for key in func:
            if func[key]>=0:
                mylist.append(func[key])
        if not mylist:
            return -1
        else:
            return min(mylist)
                
        