class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        nums = [i - int(str(i)[::-1]) for i in nums]
        res = 0
        temp = Counter(nums).values()
        for n in temp:
            res += n*(n-1)//2 
        return res % (10**9 + 7)
    
    
   