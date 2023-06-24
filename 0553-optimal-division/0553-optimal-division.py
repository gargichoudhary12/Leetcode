class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        list_length=len(nums)
        if list_length==1:
            return str(nums[0])
        elif list_length==2:
            return str(nums[0])+'/'+str(nums[1])
        else:
            res=str(nums[0])+'/('+str(nums[1])
            for i in range(2,list_length):
                res+='/'+str(nums[i])
            res+=')'
            return res
        