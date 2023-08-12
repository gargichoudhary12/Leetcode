class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = 0
        countone = 0
        for c in s:
            if c=="1":
                countone+=1
            else:
                res = min(res+1, countone)
        return res