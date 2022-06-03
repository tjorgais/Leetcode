class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        m=len(trust)
        func={}
        if m==0 and n==1:
            return 1
        if m==0 and n>1:
            return -1
        for i in range(m):
            x=trust[i][1]
            if x not in func:
                func[x]=0
                j=0
                seen=False
                while(j!=m):
                    if trust[j][1]==x and trust[j][0]!=x:
                        func[x]+=1
                    elif trust[j][0]==x:
                        seen=True

                    j+=1
                if func[x]==n-1 and seen==False:
                    return x
            else: 
                continue
        return -1
                    
                
        