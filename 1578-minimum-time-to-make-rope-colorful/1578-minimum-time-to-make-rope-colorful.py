class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n=len(colors)
        l=0
        ans=0
        for r in range(n):
            if (colors[r]!=colors[l]):
                same=neededTime[l:r]
                ans+=sum(same)-max(same)
                l=r
        ans+=sum(neededTime[l:])-max(neededTime[l:])
        return ans