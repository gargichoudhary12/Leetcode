class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        numbers=''.join(map(str, nums))
        ans = numbers.split('0')
        count = 0
        for i in ans:
            if len(i)>count:
                count = len(i)
        return count