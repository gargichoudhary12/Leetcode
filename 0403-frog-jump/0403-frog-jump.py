class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        lastStone = stones[-1]
        stones = set(stones)
        
        @lru_cache(None)
        def helper(stone, k):
            if stone == lastStone:
                return True
            
            return ((k != 1 and stone + k - 1 in stones and helper(stone + k - 1, k - 1)) or
                    (stone + k in stones and helper(stone + k, k)) or
                    (stone + k + 1 in stones and helper(stone + k + 1, k + 1)))
        
        return helper(1, 1)