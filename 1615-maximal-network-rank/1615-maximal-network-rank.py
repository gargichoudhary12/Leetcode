class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = collections.defaultdict(set)
        for a, b in roads:
            g[a].add(b)
            g[b].add(a)
        return max(len(g[a]) + len(g[b]) - (b in g[a])
                    for a in range(n) 
                    for b in range(a + 1, n))