class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        a=(purchaseAmount//10)*10
        b=a+10
        if purchaseAmount-a>=b-purchaseAmount:
            return abs(100-b)
        else:
            return abs(100-a)