class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        for i in range(len(v[0])):
            for s in v:
                if i == len(s) or s[i]!=v[0][i]:
                    return ans
            ans+=v[0][i]
        return ans
                