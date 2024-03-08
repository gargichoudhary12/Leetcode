class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        list_nums=list(set(nums))
        freq=0
        for i in list_nums:
            freq=max(freq,nums.count(i))
        ans=0
        for i in list_nums:
            if nums.count(i)==freq:
                ans+=freq

        return ans