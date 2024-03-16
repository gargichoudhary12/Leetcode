class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count=0
        dic={}
        n=len(nums)
        dic[0]=-1
        for i in range(n):
            nums[i]=-1 if nums[i]==0 else 1
            if(i>0):
                nums[i]=nums[i]+nums[i-1]
            if nums[i] not in dic:
                dic[nums[i]]=i
            if nums[i] in dic:
                count=max(count,i-dic[nums[i]])
        return count