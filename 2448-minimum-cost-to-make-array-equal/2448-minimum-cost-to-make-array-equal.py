class Solution(object):
    def minCost(self, nums, cost):
        n = len(nums)
        v = []
        totalCost = 0

        for i in range(n):
            v.append((nums[i], cost[i]))
            totalCost += cost[i]

        v.sort() 

        mid = (totalCost + 1) // 2
        target = -1
        currSum = 0 

        for i in range(n):
            currSum += v[i][1]
            if currSum >= mid:
                target = v[i][0] 
                break

        ans = 0
        for i in range(n):
            ans += abs(nums[i] - target) * cost[i]

        return ans