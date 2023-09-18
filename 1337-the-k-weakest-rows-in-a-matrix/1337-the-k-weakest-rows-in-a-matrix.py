class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []                           
        for i, r in enumerate(mat):
            res.append((sum(r), i))     
        res.sort()                    
        return [y for x,y in res[:k]]  