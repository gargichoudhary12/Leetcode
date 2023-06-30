class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        arr = [grid[i][j] for i in range(m) for j in range(n)]
        k = k % len(arr)
        arr = arr[-k : ] + arr[: -k]
        res = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = arr[i * n + j]
        return res