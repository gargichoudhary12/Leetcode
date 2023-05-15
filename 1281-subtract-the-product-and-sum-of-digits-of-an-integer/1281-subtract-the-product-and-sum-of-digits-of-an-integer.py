class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n != 0:
            lastDigit = n % 10
            product *= lastDigit
            sum += lastDigit
            n = n // 10
        return product - sum