class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1 : return 0 # edge cases
        prod = 1
        cnt = left= 0
        for right in range(len(nums)):
            prod *= nums[right] # expand window
            while prod >= k: # shrink window
                prod /= nums[left]
                left += 1
            if prod < k: 
                cnt += right - left + 1
        return cnt 
