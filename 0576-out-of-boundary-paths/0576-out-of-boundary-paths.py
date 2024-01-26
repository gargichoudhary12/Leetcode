class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = defaultdict(int)
        def dfs(i, j, s):
            if s > maxMove: return 0
            if i < 0 or j < 0 or i >= m or j >= n: return 1
            if (i, j, s) in memo: return memo[(i, j, s)]
            memo[(i, j, s)] = (dfs(i+1, j, s+1) +
                               dfs(i-1, j, s+1) +
                               dfs(i, j+1, s+1) +
                               dfs(i, j-1, s+1))
            return memo[(i, j, s)]
        return dfs(startRow, startColumn, 0) % (10**9+7)