class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        M = P = G = 0
        res = 0
        for i,gar in enumerate(garbage):
            count =Counter(gar)
            if count['G']!=0:
                G = i
            if count['P']!=0:
                P = i
            if count['M']!=0:
                M = i
            res += sum(count.values())
        res += sum(travel[:M])
        res += sum(travel[:P])
        res += sum(travel[:G])
        return res