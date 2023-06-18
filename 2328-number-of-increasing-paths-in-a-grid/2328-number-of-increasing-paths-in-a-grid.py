class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        DIRS = ((-1, 0), (1, 0), (0, 1), (0, -1))
        MOD = int(1e9+7)
        @cache
        def search(row: int, col: int) -> int:
            """Given this row and column, how many paths stem from here?"""
            count = 1 # Just visit the node itself
            for dr, dc in DIRS:
                if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
                    # Must be strictly increasing
                    if not grid[row + dr][col + dc] > grid[row][col]:
                        continue
                    count += search(row + dr, col + dc)
            return count % MOD
        return sum(search(row, col) for row in range(len(grid)) for col in range(len(grid[0]))) % MOD