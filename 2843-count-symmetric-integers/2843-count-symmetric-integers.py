class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=0
        for i in range(low,high+1):
            x = str(i)
            if len(x)%2==0:
                if sum(list(map(int,x[:len(x)//2]))) == sum(list(map(int,x[len(x)//2:]))):
                    res+=1
                    
        return res
        