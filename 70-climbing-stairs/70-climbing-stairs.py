class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        L=[0 for i in range(n+1)]
        L[1]=1
        L[2]=2
        for i in range(3,n+1):
            L[i]=L[i-1]+L[i-2]
        return L[n]

        