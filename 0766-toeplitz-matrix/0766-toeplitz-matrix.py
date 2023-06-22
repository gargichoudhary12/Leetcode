class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i>0 and j>0 and matrix[i-1][j-1]!=matrix[i][j]:
                    return False
        return True
            