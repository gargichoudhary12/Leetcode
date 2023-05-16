class Solution:
    def numberOfSteps(self, num: int) -> int:
        a,b=0,0
        while num:
            a+=num%2
            b+=1
            num//=2
        if a+b>0:
            return a+b-1 
        else:
            return 0