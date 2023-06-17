import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        A = np.transpose(matrix)
        arr=[]
        #print(A)
        for i in range(len(A)):
            temp=A[i]
            temp=temp[::-1]
            arr.append(list(temp))
            matrix[i]=list(temp)

        
        

    