class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        v = []
        n = len(grid)
        for i in range (n):
            for j in range (n):
                v.append(grid[i][j])
        
        v.sort()

        missing = 1
        repeat = 0

        for i in range (len(v)):
            if missing == v[i]:
                missing += 1
            if i != 0 and v[i] == v[i-1]:
                repeat = v[i]

        return [repeat, missing]