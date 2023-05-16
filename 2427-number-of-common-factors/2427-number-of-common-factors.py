class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum([(a % n == 0 and b % n == 0) for n in range(1, gcd(a, b) + 1)])