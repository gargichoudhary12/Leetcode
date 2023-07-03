class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if s == goal:
            temp = set(s)
            return len(temp)<len(goal)
        l=0
        r=n-1
        while l<r and s[l]==goal[l]:
            l+=1
        while r>=0 and s[r]==goal[r]:
            r-=1
        if l<r:
            slist = list(s)
            slist[l], slist[r]=slist[r],slist[l]
            s = ''.join(slist)
        return s ==goal
        