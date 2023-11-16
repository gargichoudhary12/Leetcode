class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        ans=['1']*n
        for i, j in enumerate(nums):
            ans[i]=chr(ord('1')-ord(j[i])+ord('0'))
        return "".join(ans)