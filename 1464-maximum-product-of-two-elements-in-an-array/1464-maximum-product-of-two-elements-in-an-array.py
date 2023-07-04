class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lst = sorted(nums)
        return (lst[-1]-1)*(lst[-2]-1)