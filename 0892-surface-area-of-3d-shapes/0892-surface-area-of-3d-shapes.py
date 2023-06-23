class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        sum=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]>0):
                    sum+=grid[i][j]*4+2
                    if(i>0):
                        sum-=min(grid[i][j],grid[i-1][j])*2
                    if(j>0):
                        sum-=min(grid[i][j],grid[i][j-1])*2
        return sum