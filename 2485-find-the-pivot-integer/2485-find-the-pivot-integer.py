class Solution:
    def pivotInteger(self, n: int) -> int:
        A = n*(n+1)//2
        for x in range(n+1):
            B = x*(x-1)//2
            C = x*(x+1)//2
            if A - B == C: return x
        return -1