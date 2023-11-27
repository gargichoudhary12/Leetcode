class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans =   (n+2)*(n+1)//2
        if (n:= n - limit-1) < 0: 
            return ans
        ans-= 3*(n+2)*(n+1)//2
        if (n:= n - limit-1) < 0: 
            return ans
        ans+= 3*(n+2)*(n+1)//2
        if (n:= n - limit-1) < 0: 
            return ans
        ans-=   (n+2)*(n+1)//2
        return ans