class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False]*(len(nums)+1)
        dp[-1] = True 
        for i in range(len(nums)-1, -1, -1): 
            if i+1 < len(nums) and dp[i+2] and nums[i] == nums[i+1] \
            or i+2 < len(nums) and dp[i+3] and (nums[i] == nums[i+1] == nums[i+2] or nums[i]+2 == nums[i+1]+1 == nums[i+2]): dp[i] = True
        return dp[0]