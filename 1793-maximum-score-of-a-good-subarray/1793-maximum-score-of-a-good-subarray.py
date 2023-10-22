class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        score, minNum = nums[k], nums[k]
        l = r = k
        length = len(nums)
        while True:
            while l > 0 and nums[l-1] >= minNum:
                l -= 1
            while r < length-1 and nums[r+1] >= minNum:
                r += 1
            score = max(score, minNum*(r-l+1))
            if l == 0 and r == length-1:
                return score
            elif l == 0:
                r += 1
                minNum = nums[r]
            elif r == length-1:
                l -= 1
                minNum = nums[l]
            else:
                if nums[l-1] > nums[r+1]:
                    l -= 1
                    minNum = nums[l]
                else:
                    r += 1
                    minNum = nums[r]