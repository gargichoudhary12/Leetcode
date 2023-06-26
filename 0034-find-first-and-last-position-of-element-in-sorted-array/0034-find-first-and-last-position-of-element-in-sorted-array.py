class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        left=0
        right= len(nums)-1        
        while left<=right:
            mid=left+(right-left+1)//2
            if nums[mid] == target:
                start = end = mid
                while start > 0 and nums[start - 1] == target:
                    start -= 1
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                
                return [start, end]
                    
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return [-1,-1]
    
    
