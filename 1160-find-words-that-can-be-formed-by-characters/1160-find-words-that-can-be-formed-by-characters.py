class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(len(word) if collections.Counter(word) <= collections.Counter(chars) else 0 for word in words)
        