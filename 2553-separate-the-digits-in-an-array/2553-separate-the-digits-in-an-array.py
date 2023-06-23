class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for x in nums:
            ans=[]
            while x>0:
                ans.insert(0,x%10)
                x=x//10
            res+=ans
        return res
        