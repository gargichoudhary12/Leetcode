class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l<=r:
            m = (l+r)//2
            if (arr[m+1]<arr[m] and arr[m-1]<arr[m]):
                return m
            elif arr[m+1]>arr[m]:
                l = m+1
            else:
                r = m
        
        