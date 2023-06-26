class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = (mainTank + min((mainTank-1)//4,additionalTank))
        return int(10*res)