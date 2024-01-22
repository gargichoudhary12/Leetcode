class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        diff = len(nums)*(len(nums)+1)//2
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0: dup = num
            else:   nums[num-1] = -nums[num-1]
            diff -= num
        return [dup, dup+diff]