class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        DP = [[0]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            DP[i][0] = 1
        for i in range(2, n+1):
            for j in range(1, k+1):
                if (j-1)-(i-1) >= 0:
                    DP[i][j] = (DP[i][j-1] + DP[i-1][j] - DP[i-1][(j-1)-(i-1)])%(10**9+7)
                else:
                    DP[i][j] = (DP[i][j-1] + DP[i-1][j])%(10**9+7)
        return DP[-1][-1]