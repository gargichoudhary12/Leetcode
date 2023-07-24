class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        square = []
        for side in rectangles:
            square.append(min(side[0],side[1]))
        return square.count(max(square))