class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x<=n:
            if x!=n:
                x = x*2
            else:
                return True
        return False
        