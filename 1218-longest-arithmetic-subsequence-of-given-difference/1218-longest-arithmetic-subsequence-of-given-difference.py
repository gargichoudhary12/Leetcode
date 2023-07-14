class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        digits = {}
        count = 0
        for i in range(len(arr)):
            first = arr[i]
            if first-difference in digits:
                digits[first] = digits[first-difference]+1
            else:
                digits[first]=1
            count = max(count, digits[first])
        return count
        