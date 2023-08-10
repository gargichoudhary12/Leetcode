class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff=(sum(aliceSizes)-sum(bobSizes))//2;
        A=set(aliceSizes)
        for i in set(bobSizes):
            if i+diff in aliceSizes:
                return [diff+i,i]