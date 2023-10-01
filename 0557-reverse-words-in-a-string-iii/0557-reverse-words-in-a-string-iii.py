class Solution:
    def reverseWords(self, s: str) -> str:
        s=s[::-1].split()
        return " ".join(s[::-1])