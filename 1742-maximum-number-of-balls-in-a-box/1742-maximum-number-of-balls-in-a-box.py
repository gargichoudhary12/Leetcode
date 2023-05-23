class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count, mx = [0] * 46, 0
        for i in range(lowLimit, highLimit + 1):
            sm = 0
            while i > 0:
                sm += i % 10
                i //= 10
            count[sm] += 1
            mx = max(mx, count[sm])
        return mx