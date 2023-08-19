class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                perimeter += 4*grid[i][j]
                if i>0:
                    perimeter-=grid[i][j]*grid[i-1][j]
                if i<len(grid)-1:
                    perimeter -=grid[i][j]*grid[i+1][j]
                if j>0:
                    perimeter-=grid[i][j]*grid[i][j-1]
                if j<len(grid[0])-1:
                    perimeter-=grid[i][j]*grid[i][j+1]
        return perimeter