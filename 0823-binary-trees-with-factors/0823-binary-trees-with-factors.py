class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        m = 10**9+7
        arr.sort()
        idx = {}
        for i,j in enumerate(arr):
            idx[j] = i
        dp = [1 for _ in range(len(arr))]
        for i in range(1,len(arr)):
            for j in range(i):
                if arr[i]%arr[j] == 0:
                    if arr[i]//arr[j] in idx:
                        dp[i] += dp[idx[arr[i]//arr[j]]]*dp[j]
                        dp[i] %= m
        return sum(dp)%m