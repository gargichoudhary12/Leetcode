class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        root = int(math.sqrt(area))
        for l in range(root, 1, -1):
            if not area % l:
                x, y = min(l, area // l), max(l, area // l)
                return [y, x]   
        return [area, 1]