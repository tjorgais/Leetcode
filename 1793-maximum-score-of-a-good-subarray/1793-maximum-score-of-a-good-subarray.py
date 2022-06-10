class Solution:
    def maximumScore(self, num: List[int], k: int) -> int:
        n=len(num)
        Sol=num[k]
        Min=num[k]
        i,j=k,k
        while i>0 and j+1<n:
            if num[i-1]>num[j+1]:
                Min=min(Min,num[i-1])
                i-=1
            else:
                Min=min(Min, num[j+1])
                j+=1
            Sol=max(Sol, Min*(j-i+1))
        while i>0:
            Min=min(Min,num[i-1])
            i-=1
            Sol=max(Sol, Min*(j-i+1))
        while j+1<n:
            Min=min(Min, num[j+1])
            j+=1
            Sol=max(Sol, Min*(j-i+1))
        return Sol
        
        