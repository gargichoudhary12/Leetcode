class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        remaining = list(accumulate(piles[::-1]))[::-1]
        @lru_cache(None)
        def dp(i, m):
            if i + 2*m >= len(piles):
                return remaining[i]
            return remaining[i] - min(dp(i+x, max(m, x)) for x in range(1, min(2*m+1, len(piles)-i)))
        return dp(0, 1)
