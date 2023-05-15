class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        dict_ = {}
        dict_['col'] = [0]*n
        dict_['row'] = [0]*m
        for idx in range(len(indices)):
            dict_['row'][indices[idx][0]] += 1
            dict_['col'][indices[idx][1]] += 1
        count_odd = 0
        for row in range(m):
            for col in range(n):
                if (dict_['row'][row] + dict_['col'][col])&1 == 1:
                    count_odd += 1
        return count_odd