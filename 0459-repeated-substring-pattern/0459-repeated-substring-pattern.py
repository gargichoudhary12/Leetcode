class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
         return s in s[1:] + s[:-1]