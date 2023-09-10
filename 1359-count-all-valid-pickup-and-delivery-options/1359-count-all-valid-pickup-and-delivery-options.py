class Solution:
    def countOrders(self, n: int) -> int:
        count = 1
        mod = 10**9+7
        for i in range(2, n+1):
            count = ((2*i*i-i)*count)%mod
        return count