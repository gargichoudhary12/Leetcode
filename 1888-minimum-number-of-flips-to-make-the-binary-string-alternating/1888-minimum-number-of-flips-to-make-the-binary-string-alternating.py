class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        odd = even = 0
        for i, ch in enumerate(s):
            if ch == '0':
                continue
            
            if i % 2 == 1:
                odd += 1
            else:
                even += 1
        
        if n % 2 == 0:
            res = min(n // 2 - odd + even, n // 2 - even + odd)
        else:
            res = min((n - 1) // 2 - odd + even, (n + 1) // 2 - even + odd)
            for i in range(n):
                if s[i] == '0':
                    odd, even = even, odd
                else:
                    odd, even = even - 1, odd + 1
                temp = min((n - 1) // 2 - odd + even, (n + 1) // 2 - even + odd)
                res = min(res, temp)
        return res