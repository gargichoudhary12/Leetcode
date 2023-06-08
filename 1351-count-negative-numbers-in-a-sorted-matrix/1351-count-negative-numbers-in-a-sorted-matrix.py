class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row=len(grid[0])
        col=len(grid)
        
        i=0
        j=row-1
        total=0
        while i<col and j>=0:
            if grid[i][j]<0:
                total+=col-i
                j-=1
                
            else:
                i+=1
                
        return total