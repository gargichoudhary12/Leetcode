class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        def helper(i):
            if i>=len(questions):
                return 0
            if i in dp:
                return dp[i]
            
            dp[i]=max(helper(i+1), questions[i][0]+helper(i+1+questions[i][1]))
            return dp[i]
        return helper(0)