class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        arr = [(1,1)]*len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    if arr[j][0]+1 > arr[i][0]:
                        arr[i] = (arr[j][0]+1, arr[j][1])
                    elif arr[j][0]+1 == arr[i][0]:
                        arr[i] = (arr[i][0], arr[j][1]+arr[i][1])
        
        longest = max(length for length, _ in arr)
        count = 0
        for length, c in arr:
            if length==longest:
                count += c
        return count
        