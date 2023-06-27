class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n

        leastX = min(op[0] for op in ops)
        leastY = min(op[1] for op in ops)

        return (leastX * leastY)