class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        ans, pq = set(), [(0, points[0][0], points[0][1], 0)]
        while pq and len(ans) < n:
            dist, x1, y1, idx = heappop(pq)
            if idx in ans: 
                continue
            ans.add(idx)
            res += dist
            for i in range(n):
                if i in ans: 
                    continue
                x2, y2 = points[i]
                heappush(pq, (abs(x1-x2) + abs(y1-y2), x2, y2, i))
            
        return res