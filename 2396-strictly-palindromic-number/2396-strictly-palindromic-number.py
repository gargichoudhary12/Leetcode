class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            res = ''
            num = n
            while num:
                rem = num % i
                num = num // i
                res += str(rem)
            if res != res[::-1]:
                return False
        return True