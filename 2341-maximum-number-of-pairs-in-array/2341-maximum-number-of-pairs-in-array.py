class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = 0
        left = 0
        for num in set(nums):
            c = nums.count(num)
            if c >= 2:
                pairs += (c // 2)
                if c % 2 != 0:
                    left += 1
            else:
                left += 1
        return [pairs, left]