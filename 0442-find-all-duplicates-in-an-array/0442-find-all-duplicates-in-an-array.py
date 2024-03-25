class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=[]
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                l.append(nums[i])
            d[nums[i]]=1
        return l