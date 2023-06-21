class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = min(nums)
        m = max(nums)
        return next((num for num in nums if num not in (n, m)), -1)
        