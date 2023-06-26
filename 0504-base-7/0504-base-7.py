class Solution:
    def convertToBase7(self, num: int) -> str:
        n= abs(num)
        s=''       
        while n>0:
            remaining=n%7
            n=n//7
            s = str(remaining)+s 

        if num<0:
            s="-"+s
        if num==0:
            s='0'
        return s