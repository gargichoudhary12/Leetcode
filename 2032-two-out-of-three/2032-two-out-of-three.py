class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans=[]
        nums={}
        for i in nums1:
            if(i not in nums):
                nums[i]=1
        for i in nums2:
            if(i in nums):
                if(nums[i]==1):
                    ans.append(i)
                    nums[i]=0
            else:
                nums[i]=2
        for i in nums3:
            if(i in nums):
                if(nums[i]==1 or nums[i]==2):
                    ans.append(i)
                    nums[i]=0
        return ans