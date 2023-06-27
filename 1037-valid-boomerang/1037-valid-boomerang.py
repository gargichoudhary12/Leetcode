class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        x3, y3 = points[2][0], points[2][1]
        slope12 = 0
        if x2 - x1 == 0:
            slope12 = 90
        else:
            slope12 = (y2 - y1) / (x2 - x1)
        slope13 = 0
        if x3 - x1 == 0:
            slope13 = 90
        else:
            slope13 = (y3 - y1) / (x3 - x1)
        slope23 = 0
        if x3 - x2 == 0:
            slope23 = 90
        else:
            slope23 = (y3 - y2) / (x3 - x2)

        if slope12 == slope13 or slope12 == slope23 or slope13 == slope23:
            return False
        return True