class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        j=0
        for i in index:
            target.insert(i,nums[j])
            j+=1
        return (target)