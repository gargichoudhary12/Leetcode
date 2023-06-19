class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = current
        for i in gain:
            current += i
            highest = max(highest, current)
        return highest
        