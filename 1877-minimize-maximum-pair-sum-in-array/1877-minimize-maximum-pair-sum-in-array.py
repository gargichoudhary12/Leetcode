class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pairs = []
        nums.sort()
        pt1 = 0
        pt2 = len(nums)-1
        while True:
            if pt2 < pt1 or pt1 > pt2:
                break
            pairs.append([nums[pt1],nums[pt2]])
            pt1 += 1
            pt2 -= 1
        pairs = [sum(i) for i in pairs]
        return max(pairs)