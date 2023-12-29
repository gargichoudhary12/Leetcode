class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        cache = {}
        J = len(jobDifficulty)
        def dp(idx, day):
            if idx == J:
                if day == d:
                    return 0
                else:
                    return float('inf')
            
            if day == d:
                return float('inf')
            
            if (idx, day) in cache:
                return cache[(idx, day)]
            
            res = float('inf')
            curr = 0
            for i in range(idx, J):
                curr = max(curr, jobDifficulty[i])
                res = min(res, curr + dp(i + 1, day + 1))
            cache[(idx, day)] = res
            return res
        res = dp(0,0)
        return res if res != float('inf') else -1