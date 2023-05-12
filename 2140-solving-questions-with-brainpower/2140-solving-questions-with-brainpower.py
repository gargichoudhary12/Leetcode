class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            p, b = questions[i]
            if i + b + 1 < n:
                dp[i] = max(p + dp[i + b + 1], dp[i + 1])
            else:
                dp[i] = max(p, dp[i + 1])

        return dp[0]
        