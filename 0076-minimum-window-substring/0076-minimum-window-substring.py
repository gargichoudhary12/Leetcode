from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        chars, count, min_size, min_start = Counter(t), len(t), float('inf'), -1
        l = r = 0
        for r in range(len(s)):
            if chars[s[r]] >= 1:
                count -= 1
            chars[s[r]] -= 1
            while l<len(s) and count == 0:
                if chars[s[l]] >= 0:
                    if r-l+1 < min_size:
                        min_size = r-l+1
                        min_start = l
                    count += 1 
                chars[s[l]] += 1
                l += 1

        return s[min_start:min_start+min_size] if min_start > -1 else ""
        