class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        def division(dividend, divisor):
            while dividend%divisor ==0:
                dividend//=divisor
            return dividend
        for i in [2,3,5]:
            n = division(n, i)
        return n ==1
        