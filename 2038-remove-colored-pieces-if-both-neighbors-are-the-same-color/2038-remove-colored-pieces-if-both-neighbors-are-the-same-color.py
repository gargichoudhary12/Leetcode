class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        movesA, movesB = 0,0
        curA , curB = 0,0
        for i in range(n):
            if colors[i] == 'A':
                if curB > 2:
                    movesB += curB-2
                curB= 0
                curA += 1
            else:
                if curA > 2:
                    movesA += curA-2
                curA = 0
                curB += 1
        if curA > 2:
            movesA += curA-2
        if curB > 2 :
            movesB += curB-2
        return True if movesA > movesB else False