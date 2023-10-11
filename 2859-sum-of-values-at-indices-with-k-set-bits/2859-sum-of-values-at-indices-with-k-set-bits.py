class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        self.nums=nums
        self.k=k
        l=len(nums)
        sum=0
        for i in range(0,l):
            a=bin(i).count('1')
            if a==k:
                sum=sum+nums[i]
        return sum