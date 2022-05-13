def binarySearch(arr, l, r,m):
    if r >= l:

        mid = l + (r - l) // 2

        if arr[mid] <0:
            if mid==0:
                return m
            elif arr[mid-1]>=0:
                return m-mid
            else:
                return binarySearch(arr, l,mid-1,m)
        else:
            return binarySearch(arr, mid + 1, r, m)

    else:
        return 0

class Solution:

        
    def countNegatives(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        count=0
        for i in range(n):
            count+=binarySearch(grid[i],0,m-1,m)

        return count
        