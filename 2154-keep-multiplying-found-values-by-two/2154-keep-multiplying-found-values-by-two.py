class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if original in nums:
                original=original*2
        return original