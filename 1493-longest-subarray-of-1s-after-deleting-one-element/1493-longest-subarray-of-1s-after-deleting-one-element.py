class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        zero = 0
        count = 0
        for right in range(n):
            if nums[right]==0:
                zero+=1
            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            count = max(count, right - left)
        return count

        