class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positiveCount = 0
        negativeCount = 0
        for i in range(len(nums)):
            if nums[i]>0:
                positiveCount+=1
            elif nums[i]<0:
                negativeCount+=1
            elif nums[i]==0:
                continue
            i+=1
        return max(positiveCount, negativeCount)