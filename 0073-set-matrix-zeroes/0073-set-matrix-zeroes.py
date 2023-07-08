class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRowValue = 1
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0 # mark column
                    if i != 0:       
                        matrix[i][0] = 0
                    else:
                        firstRowValue = 0
        
        for i in reversed(range(ROWS)):
            for j in reversed(range(COLS)):
                if i == 0:
                    matrix[i][j] *= firstRowValue
                elif matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0