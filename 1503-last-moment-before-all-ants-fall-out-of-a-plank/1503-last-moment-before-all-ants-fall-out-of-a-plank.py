class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(n - min(right or [n]), max(left or [0]))