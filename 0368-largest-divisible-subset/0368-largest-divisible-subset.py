class Solution:
    def largestDivisibleSubset(self, a: List[int]) -> List[int]:
        a.sort()
        n=len(a)
        dp=[1]*n
        lastindex=0
        maxi=-1
        hash=[i for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                if a[i]%a[j]==0 and 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
                    hash[i]=j

            if maxi<dp[i]:
                maxi=dp[i]
                lastindex=i
        k=[a[lastindex]]
        while(lastindex!=hash[lastindex]):
            lastindex=hash[lastindex]
            k.append(a[lastindex])
        return k[::-1]
