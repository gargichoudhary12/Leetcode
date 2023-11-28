class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n,m=len(mat),len(mat[0])
        k,c=k%m,0
        if k==0:
            return True
        for i in range(n):
            if i&1:
                if mat[i][k:]+mat[i][:k] != mat[i]:
                    return False
            else:
                if mat[i][-k:]+mat[i][:-k] != mat[i]:
                    return False
        return True