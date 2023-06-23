import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n = min(nums)
        m = max(nums)
        return gcd(n,m)
        