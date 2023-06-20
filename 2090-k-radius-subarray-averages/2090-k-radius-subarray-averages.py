class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res = []
        for i in range(len(nums)):
            if i - k < 0 or i + k >= len(nums):
                res.append(-1)
            else:
                res.append((nums[i + k] - (0 if i == k else nums[i - k - 1])) // (2 * k + 1))
        return res