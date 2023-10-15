class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        n =  min(steps // 2 + 1, arrLen)
        dp = [0] * n
        dp[0] = 1
        for step in range(steps):
            dp1 = [0] * n
            for i in range(min(step + 2, n)):
                if i - 1 >= 0: dp1[i] += dp[i - 1]
                if i + 1 < n: dp1[i] += dp[i + 1]
                dp1[i] = (dp[i] + dp1[i]) % mod
            dp = dp1
        return dp[0]