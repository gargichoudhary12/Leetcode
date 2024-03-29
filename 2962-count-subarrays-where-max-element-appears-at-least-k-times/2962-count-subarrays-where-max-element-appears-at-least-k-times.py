class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = {}
        n = len(nums)
        a = max(nums)
        i = j = 0
        ans = 0
        while j < n:
            m[nums[j]] = m.get(nums[j], 0) + 1
            while m.get(a, 0) >= k:
                ans += n - j
                m[nums[i]] -= 1
                i += 1
            j += 1
        return ans
