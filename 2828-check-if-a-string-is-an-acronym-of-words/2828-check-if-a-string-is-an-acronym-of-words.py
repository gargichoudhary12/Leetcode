class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        a=''.join([i[0] for i in words])
        return s==a