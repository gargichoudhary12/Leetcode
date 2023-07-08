class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        elif n==3:
            return 2
        elif n==4:
            return 4
        x = n%3
        if x == 0:
            return int(3**(n/3))
        elif x==1:
            return int(4*3**((n-1)/3-1))
        elif x==2:
            return int(2*3**((n-2)/3))