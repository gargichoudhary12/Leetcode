class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        res = pow(10,5)+1;
        count = 0;
        for i in range(0,len(nums)):
            count += nums[i]
            while( count >= target ):
                if(i-start+1<res):
                    res = i-start+1
                count -= nums[start];
                start += 1;
        if(res==pow(10,5)+1): 
            return 0;
        return res;