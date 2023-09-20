class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l = 0
        ans = 0
        n = len(nums)
        if sum(nums)<x:
            return -1
        elif sum(nums)==x:
            return n
        
        res = n+1
        while l<n:
            ans+=nums[l]
            if ans ==x:
                res = l+1
                break
            elif ans>x:
                break
            l+=1
        if l==n:
            return -1
        r = n-1
        while r>l and l>=-1:
            temp = nums[r]+ans
            if temp>x and l>=0:
                ans-=nums[l]
                l-=1
            elif temp==x:
                res = min(res, l+1+n-r)
                ans = temp
                r-=1
            else:
                ans = temp
                r-=1
        if res<n:
            return res
        else:
            return -1