class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        @lru_cache(None)
        def dfs(row, left, right):
            if row not in range(m): return 0
            if left not in range(n) or right not in range(n) or left >= right: return -inf

            return  (grid[row][left] + grid[row][right] +
                       max(dfs(row+1, left+i, right+j) for i in moves for j in moves))


        m, n = len(grid), len(grid[0])
        moves = (-1,0,1)
        return dfs(0, 0, n-1)