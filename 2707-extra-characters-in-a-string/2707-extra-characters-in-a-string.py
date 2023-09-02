class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dict_set = set()
        for word in dictionary:
            dict_set.add(len(word))
        dp = [0] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1] + 1
            for word_len in dict_set:
                if i >= word_len and s[i - word_len : i] in dictionary:
                    dp[i] = min(dp[i], dp[i - word_len])
        return dp[len(s)]