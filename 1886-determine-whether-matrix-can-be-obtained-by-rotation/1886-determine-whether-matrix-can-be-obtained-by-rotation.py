class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        s = n
        x = (int)(n // 2)
        if mat==target:
            return True
        else:
            for i in range(3):
                for i in range(0, x):
                    for j in range(i, n - i - 1):
                        temp1 = mat[i][j]
                        temp2 = mat[j][n - i - 1]
                        temp3 = mat[n - i - 1][n - j - 1]
                        temp4 = mat[n - j - 1][i]
                        mat[i][j] = temp4
                        mat[j][n - i - 1] = temp1
                        mat[n - i - 1][n - j - 1] = temp2
                        mat[n - j - 1][i] = temp3
                if mat==target:
                    return True
                    break
        return False
        