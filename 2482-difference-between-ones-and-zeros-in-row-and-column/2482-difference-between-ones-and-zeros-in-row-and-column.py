class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        num_ones_rows = []
        num_zeros_rows = []
        num_ones_cols = []
        num_zeros_cols = []
        
        for i in range(n):
            counter, counter2 = 0, 0
            for j in range(m):
                counter += 1 if grid[i][j] == 1 else 0
                counter2 += 1 if grid[i][j] == 0 else 0
            num_ones_rows.append(counter)
            num_zeros_rows.append(counter2)
        
        for a in range(m):
            counter3, counter4 = 0, 0
            for b in range(n):
                counter3 += 1 if grid[b][a] == 1 else 0 
                counter4 += 1 if grid[b][a] == 0 else 0
            num_ones_cols.append(counter3)
            num_zeros_cols.append(counter4)
        
        ans = [[] for _ in range(n)]
        
        for c in range(n):
            for d in range(m):
                answer = num_ones_rows[c] + num_ones_cols[d] - num_zeros_rows[c] - num_zeros_cols[d]
                ans[c].append(answer)
                
        return ans