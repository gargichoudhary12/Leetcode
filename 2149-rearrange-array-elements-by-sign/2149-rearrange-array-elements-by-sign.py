class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos_i, neg_i = 0, 1
        
        for num in nums:
            if num > 0:
                res[pos_i] = num
                pos_i += 2
            else:
                res[neg_i] = num
                neg_i += 2
        
        return res