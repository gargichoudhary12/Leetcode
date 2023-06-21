class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        totalSum = 0
        timesSeen = {}
        for num in nums:
            if num not in timesSeen:
                totalSum += num
                timesSeen[num] = 1
            elif num in timesSeen:
                if timesSeen[num] == 1:
                    totalSum -= num
                timesSeen[num] += 1
            
        return totalSum
