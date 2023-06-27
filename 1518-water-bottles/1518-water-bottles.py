class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles >= numExchange:
            ans = numBottles // numExchange
            remaining = numBottles % numExchange
            total += ans
            numBottles = ans + remaining
        return total