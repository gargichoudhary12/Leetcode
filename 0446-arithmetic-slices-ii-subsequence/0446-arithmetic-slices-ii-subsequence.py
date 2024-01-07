class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n= len(nums)
        total_count = 0
        dp =[{} for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[i].get(diff,0) + dp[j][diff]
                dp[i][diff] = dp[i].get(diff,0) + 1
                total_count += dp[j].get(diff, 0)
        return total_count