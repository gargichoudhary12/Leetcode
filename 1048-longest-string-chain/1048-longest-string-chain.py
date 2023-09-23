class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp={}
        arr = sorted(words, key = len)
        for word in arr:
            temp=[0]
            n=len(word)
            for i in range(n):
                if word[:i]+word[i+1:] in dp:
                    temp.append(dp[word[:i]+word[i+1:]])
                dp[word]=max(temp)+1
        return max(dp.values()) 