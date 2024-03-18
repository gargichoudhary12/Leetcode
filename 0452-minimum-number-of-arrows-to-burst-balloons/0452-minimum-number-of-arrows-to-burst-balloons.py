class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        xstart = points[0][0]
        xend = points[0][1]
        arrow = 1
        for i in range(1,len(points)):
            if points[i][0] <= xend:
                xstart = max(xstart, points[i][0])
                xend = min(xend, points[i][1])
            else:
                arrow+=1
                xstart = points[i][0]
                xend = points[i][1]
        return arrow