class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        d = 0
        for c in s:
            if c == '(':
                d += 1
            elif c == ')':
                d = max(0, d-1)
            ans = max(ans, d)
        return ans