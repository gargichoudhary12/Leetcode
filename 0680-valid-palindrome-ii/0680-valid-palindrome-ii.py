class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL==skipL[::-1] or skipR==skipR[::-1])
            l = l+1
            r=r-1          
        return True