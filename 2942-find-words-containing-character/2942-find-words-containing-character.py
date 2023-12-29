class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            for letter in words[i]:
                if letter == x:
                    ans.append(i)
                    break
        return ans