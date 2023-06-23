class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n)
        s = s+str(2*n)+str(3*n)
        ans = set(s)
        if len(ans)==len(s)==9 and '0' not in ans:
            return True

        else:
            return False
        