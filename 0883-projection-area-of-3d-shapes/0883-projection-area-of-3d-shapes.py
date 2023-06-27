class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = 0
        for x in grid:
            res = 0
            for y in x:
                if y:
                    res = max(y,res)
                    area += 1
            area += res        
        for j in range(len(grid[0])):
            area += max(grid[i][j] for i in range(len(grid)))
        return area