class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        height, width = len(heights), len(heights[0])
        queue = [(0, 0, 0)]
        visited = set()

        while queue:
            max_diff, y, x = heappop(queue)
            if (y, x) == (height-1, width-1):
                return max_diff

            if (y, x) in visited:
                continue
            visited.add((y, x))

            for new_y, new_x in ((y+1, x), (y-1, x), (y, x+1), (y, x-1)):
                if 0 <= new_y < height and 0 <= new_x < width and (new_y, new_x) not in visited:
                    heappush(queue, (max(max_diff, abs(heights[y][x] - heights[new_y][new_x])), new_y, new_x))