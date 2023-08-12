class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sumEven = 0
        sumOdd = 0
        for i in range(len(nums)-1, -1, -1):
            tempEven = max(sumOdd + nums[i], sumEven)
            tempOdd = max(sumEven - nums[i], sumOdd)
            sumEven = tempEven
            sumOdd = tempOdd
        return sumEven
            
            