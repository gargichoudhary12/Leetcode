class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured==0:
            return 0
        glasses = [poured]
        for i in range(2,query_row+2):
            temp = [0]*i
            for j in range(len(glasses)):
                if (glasses[j]-1)/2 > 0:
                    temp[j] += (glasses[j]-1)/2
                    temp[j+1] += (glasses[j]-1)/2
            glasses = temp
        return min(1,glasses[query_glass])