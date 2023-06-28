# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        left = 0
        right = length -1
        while left<right:
            mid = (left+right)//2
            if mountain_arr.get(mid)>=mountain_arr.get(mid+1):
                right=mid
            else:
                left = mid+1
        peak = left
        if target == mountain_arr.get(peak):
            return peak
        
        l =0 
        r =peak-1
        while l<=r:
            print(l,r, end=' ')
            mid = (l+r)//2
            print('1:',mid)
            curr = mountain_arr.get(mid)
            if curr == target:
                return mid
            elif curr>target:
                r = mid-1
            else:
                l = mid+1
                
                
        l = peak+1
        r = length-1
        while l<=r:
            print('2:',mid)
            mid = (l+r)//2
            curr = mountain_arr.get(mid)
            if curr == target:
                return mid
            elif curr>target:
                l = mid+1
            else:
                r = mid-1
        return -1
        