class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums)%2==0:
            return True
        
        dp=nums[:]
        for i in range(1,len(nums)):
            for j in range(len(nums)-i):
                dp[j]=max(nums[j]-dp[j+1],nums[j+i]-dp[j])
                
        if dp[0]>=0:
            return True
        return False