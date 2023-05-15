import numpy as np
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        arr=np.zeros((m,n),dtype=int)
        for row,col in indices:
            arr[row,:]+=1
            arr[:,col]+=1
        return(len(arr[arr%2!=0]))