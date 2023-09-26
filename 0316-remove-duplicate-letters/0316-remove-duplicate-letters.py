class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = []
        remaining = Counter(s)
        
        for c in s:
            if c not in res:
                while res and res[-1] >= c and remaining[res[-1]] > 0:
                    res.pop()
                res.append(c)
            remaining[c]-=1
        
        return "".join(res)