class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        ans = []
        prev =""
        count = 0
        for i in range(len(s)):
            if prev == s[i]:
                count+=1
            else:
                ans.append(count)
                count = 1
            prev = s[i]
        ans.append(count)
        res = 0
        for num in ans:
            res = (res + (num+1) % MOD * num % MOD //2) % MOD
        return res