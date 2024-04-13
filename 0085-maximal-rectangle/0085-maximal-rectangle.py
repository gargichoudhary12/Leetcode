class Solution:
    def maximalRectangle(self, m: List[List[str]]) -> int:
        rows = len(m)
        if not rows:
            return 0
        
        cols = len(m[0])
        
        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows): # fill dp, value = number of 1s on the left side
            acc = 0
            
            for j in range(cols):
                if m[i][j] == "1":
                    acc += 1
                else:
                    acc = 0
                    
                dp[i][j] = acc
                
        res = 0
        
        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                bSide, rSide = dp[i][j], 0 # bottom and right side
                k = i
                
                while k > -1 and dp[k][j]:  # iterate all possible rectangles
                    bSide = min(bSide, dp[k][j])
                    rSide += 1

                    res = max(res, bSide * rSide)
                    
                    k -= 1
                
        return res