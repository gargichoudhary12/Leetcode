class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s, target = Counter(s), Counter(target)
        return min(s[e]//target[e] for e in target)