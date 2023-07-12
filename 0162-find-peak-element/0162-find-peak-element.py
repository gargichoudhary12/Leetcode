class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = l+((r-l)//2)
            
            #left neighbour is greater
            if (m>0 and nums[m]<nums[m-1]):
                r = m-1
                
            #right neighbour is greater
            elif (m<len(nums)-1 and nums[m]<nums[m+1]):
                l = m+1
            
            else:
                return m
        