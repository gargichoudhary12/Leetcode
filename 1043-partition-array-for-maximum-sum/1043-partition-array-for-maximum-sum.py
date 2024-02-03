class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @cache
        def dp(currIndex, currHigh, currLength):
            if currIndex == n:
                return 0
            currHigh = max(currHigh, arr[currIndex])
            currLength += 1
            if currLength == k:
                return currLength*currHigh + dp(currIndex+1, 0, 0)
            return max(currLength*currHigh + dp(currIndex+1, 0,0), dp(currIndex+1, currHigh, currLength))


        return dp(0, 0, 0)