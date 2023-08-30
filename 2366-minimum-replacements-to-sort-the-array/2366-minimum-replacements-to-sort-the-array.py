class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        prev = nums[n-1]
        for i in range(n-1, -1, -1):
            if nums[i]>prev:
                res = math.ceil(nums[i]/prev)
                count+=res-1
                prev = nums[i]//res
            else:
                prev = nums[i]
        return count