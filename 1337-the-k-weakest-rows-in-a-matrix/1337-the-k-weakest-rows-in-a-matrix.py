

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        my_arr=[]
        for i in range(n):
            count=0
            for j in range(m):
                if mat[i][j]==1:
                    count+=1
            my_arr.append([count,i])


        my_arr.sort()
        output=[]
        for i in range(k):
            output.append(my_arr[i][1])

        return output