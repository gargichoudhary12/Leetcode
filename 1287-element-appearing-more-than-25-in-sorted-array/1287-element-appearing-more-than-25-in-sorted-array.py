class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        window = len(arr) // 4        
        for left in range(len(arr)):
            right  = left + window
            if arr[left] == arr[right]:
                return arr[left]