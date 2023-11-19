class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] == nums[i]:
                continue
            ans += len(nums) - i
        return ans