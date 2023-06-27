class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0
        for i in range(k, len(s)+1):
            x = int(s[i-k:i])
            if x!=0 and num%x==0:
                count+=1
        return count
        