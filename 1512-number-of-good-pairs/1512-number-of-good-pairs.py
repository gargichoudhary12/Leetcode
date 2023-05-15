class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for index, i in enumerate(nums):
            for j in nums[index+1:]:
                if i == j:
                    count += 1
        return count