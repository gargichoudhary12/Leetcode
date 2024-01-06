class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sep = sorted([(st, en, pr) for st, en, pr in zip(startTime, endTime, profit)])
        
        @lru_cache(None)
        def dp(ci):
            
            if ci >= len(sep):
                return 0 # reached end
            
            return max(
                dp(ci + 1),
                sep[ci][2] + dp(bisect_left(sep, (sep[ci][1],)))
            )
        
        return dp(0)