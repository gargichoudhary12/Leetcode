class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        res = 0
        nums.sort()
        while ans < len(nums):
            k += nums[ans]
            if k < nums[ans] * (ans-l+1):
                k -= nums[l]
                l += 1
            res = max(res, ans - l + 1)
            ans += 1
        return res