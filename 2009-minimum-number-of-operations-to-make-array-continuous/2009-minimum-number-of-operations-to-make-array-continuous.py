from collections import deque
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque()
        max_length = 1

        for num in sorted(set(nums)):
            while q and num - q[0] >= n:
                q.popleft()

            q.append(num)
            max_length = max(max_length, len(q))

        return n - max_length