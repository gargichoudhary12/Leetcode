class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = {}
        temp = 0
        for word in words:
            if word in ans and ans[word] > 0:
                ans[word] -= 1
                temp+=1
                continue
            rev = word[::-1]
            if rev not in ans:
                ans[rev] = 0
            ans[rev] +=1
        
        return temp