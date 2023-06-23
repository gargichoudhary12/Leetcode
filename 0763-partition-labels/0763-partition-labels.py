class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c]=i
            
        res = []
        size = 0
        end = 0
        
        for i,c in enumerate(s):
            size+=1
            if lastIndex[c]>end:
                end = lastIndex[c]
            if i == end:
                res.append(size)
                size = 0
        return res
                
            