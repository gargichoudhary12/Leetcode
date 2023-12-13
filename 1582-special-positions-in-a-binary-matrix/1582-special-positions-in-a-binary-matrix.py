class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row =[]
        col = []        
        for i in range(len(mat)):
            c = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and c==0: 
                    c+=1
                    rowi = i
                elif mat[i][j] == 1 and c>=1:
                    c+=1                
            if c== 1:
                row.append(rowi)    
        print(row)
        
        for i in range(len(mat[0])):
            c = 0
            for j in range(len(mat)):
                if mat[j][i] == 1 and c==0: 
                    c+=1
                    coli = i
                elif mat[j][i] == 1 and c>=1:
                    c+=1                
            if c== 1:
                col.append(coli)
                    
        print(col)
    
        c=0
        for i in range(len(row)):
            for j in range(len(col)):
                if mat[row[i]][col[j]] == 1:
                    c+=1
      
        return c
