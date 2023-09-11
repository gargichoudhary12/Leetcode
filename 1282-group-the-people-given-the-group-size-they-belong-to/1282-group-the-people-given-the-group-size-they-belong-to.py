class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        res = []
        for i in range(len(groupSizes)):
            d[groupSizes[i]] = d.get(groupSizes[i], []) + [i]
        for k,v in d.items():
            res += [v[i:i+k] for i in range(0, len(v), k)]
        return res