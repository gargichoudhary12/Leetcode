class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=j=0
        s.sort()
        g.sort()
        while  j<len(g) and i<len(s):
            if g[j]<=s[i]:
                j+=1
            i+=1
        return j