class Solution:
    def tribonacci(self, n: int) -> int:
        n1 = 0
        n2 = 1
        n3 = 1
        if n ==0:
            return n1
        for i in range(n-2):
            n1,n2,n3 = n2,n3, (n1+n2+n3)
        return n3
        