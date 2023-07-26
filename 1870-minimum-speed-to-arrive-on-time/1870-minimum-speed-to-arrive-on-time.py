class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        start = 1
        end = 10000000 + 1
        minSpeed = -1
        while start < end:
            speed = start + (end - start)  // 2

            if (sum((dist[i] + speed - 1) // speed for i in range(len(dist) - 1)) +
                dist[-1] / speed) > hour:
                start = speed + 1
            else:
                end = speed
                minSpeed = speed
        return minSpeed