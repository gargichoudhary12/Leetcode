class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lsum = 0
        rsum = sum(nums)
        ans = []
        for i, j in enumerate(nums):
            a = i*j - lsum
            lsum += j
            rsum -= j
            a += rsum - (n-i-1)*j
            ans.append(a)
        return ans