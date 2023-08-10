class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k - (arr[-1] - len(arr)) > 0:
            return arr[-1] + k - (arr[-1] - len(arr))
        l, res = 1, []
        for i in arr:
            if i > l:
                res += [i for i in range(l,i)]
                l = i+1
            elif i == l:
                l = i + 1
        return res[k-1]