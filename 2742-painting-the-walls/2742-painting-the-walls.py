class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @cache 
        def dp(i, t):
            if i >= n: return 0 if t >= 0 else inf
            return min(dp(i+1, t-1), dp(i+1, min(n - i, t+time[i])) + cost[i])
        return dp(0, 0)