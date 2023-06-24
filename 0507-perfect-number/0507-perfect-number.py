class Solution:
    def checkPerfectNumber(self, num: int) -> bool: 
        s=1 
        i=2 
        while i*i <=num: 
            if num%i==0: 
                s=s+i+num//i 
            i+=1 
        if s==1: 
            return False
        elif s==num: 
            return True
        return False