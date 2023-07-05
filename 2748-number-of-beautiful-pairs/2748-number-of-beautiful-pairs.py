class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        c=0
        ls=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i!=j and self.gcd(int(str(nums[i])[0]),int(str(nums[j])[-1]))==1:
                    c+=1
        return c
    def gcd(self,x,y):
        while y:
            x,y=y,x%y
        return abs(x)
