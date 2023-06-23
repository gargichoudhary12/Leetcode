class Solution:
    def totalMoney(self, n: int) -> int:
        res=0
        k= 0
        for i in range(n):
            if i%7==0:
                k+=1
            res+=k+(i%7)
        return res