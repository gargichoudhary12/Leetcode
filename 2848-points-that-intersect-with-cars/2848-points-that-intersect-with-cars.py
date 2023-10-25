class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans = set()
        for i in nums:
            for j in range(i[0], i[1] + 1):
                ans.add(j)
        return len(ans)