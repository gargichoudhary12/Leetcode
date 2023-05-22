class Solution:
    def averageValue(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i%6==0:
                l.append(i)
        if len(l)>0:
            return sum(l)//len(l)  
        else:
            return 0
        