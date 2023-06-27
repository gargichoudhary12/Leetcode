class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans = ans|x
            res = ans*2**(len(nums)-1)
        return res
        