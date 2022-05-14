def my_enumerate(sequence):

    n = 0
    my_list=[]
    for elem in sequence:
        my_list.append([elem,n])
        n += 1
    return my_list

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        arr=[]
        for i in range(n):
            count=0
            for j in range(m):
                if mat[i][j]==1:
                    count+=1
                else: 
                    break
            arr.append(count)
        my_arr=my_enumerate(arr)

        my_arr.sort()
        arr.clear()
        for i in range(k):
            arr.append(my_arr[i][1])
        return arr
        