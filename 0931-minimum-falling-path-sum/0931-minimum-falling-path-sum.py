class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        arr = [[-1]*n for i in range(n)]
        arr[0] = matrix[0].copy()
        for i in range(1, n):
            for j in range(n):
                minValue = float('inf')
                for k in range(-1, 2):
                    if 0<= j + k < n: 
                        minValue = min(minValue, arr[i-1][j+k])
                arr[i][j] = matrix[i][j] + minValue
        return min(arr[n-1])