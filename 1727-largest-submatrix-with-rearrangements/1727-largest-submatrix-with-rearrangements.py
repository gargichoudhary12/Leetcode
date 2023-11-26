class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        num_of_consecutive_ones = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m):
            ones = 0
            for i in range(n-1,-1,-1):
                if matrix[i][j] == 1:
                    ones+=1
                else:
                    ones = 0
                num_of_consecutive_ones[i][j] = ones
        res = 0
        for i in range(n):
            num_of_consecutive_ones[i].sort()
            cur_min = num_of_consecutive_ones[i][-1]
            for j in range(m-1, -1, -1):
                if num_of_consecutive_ones[i][j] == 0:
                    break
                cur_min = min(cur_min, num_of_consecutive_ones[i][j])
                res = max(res, cur_min * (m - j))
        return res