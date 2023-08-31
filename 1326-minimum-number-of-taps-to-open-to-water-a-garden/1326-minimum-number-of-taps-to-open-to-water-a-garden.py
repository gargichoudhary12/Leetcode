class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        nums = [0]*(n+1)
        for i, j in enumerate(ranges):
            l = max(0, i-j)
            r = min(n, i+j)
            nums[l]=max(nums[l],r-l)
            
        ans = 0
        last = 0
        far = 0
        
        for i in range(n):
            far = max(far, i+nums[i])
            if i==last:
                ans+=1
                last = far
        return ans if last==n else -1