class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        wd=[]
        for i in range(len(points)-1):
            x1=points[i][0]
            x2=points[i+1][0]
            wd.append(x2-x1)
        return max(wd)