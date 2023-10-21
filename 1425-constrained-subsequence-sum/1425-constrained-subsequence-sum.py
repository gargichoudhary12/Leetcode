class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = collections.deque([])
        res = -float('inf')
        for i in range(len(nums)):
            if dq and i - dq[0][1] > k:
                dq.popleft()
            cur = nums[i]
            cur += dq[0][0] if dq else 0
            while dq and dq[-1][0] <= cur:
                dq.pop()
            if cur > 0:
                dq.append((cur, i))
            res = max(res, cur)
        return res