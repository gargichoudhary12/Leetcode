class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        maximum=nums[0]
        for i in nums:
            if abs(maximum)>=abs(i):
                if abs(maximum)==abs(i):
                    maximum=max(maximum,i)
                else:
                    maximum=i
        return maximum
        