class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr=[]
        temp = 0
        for i in range(n):
            s=start+(i*2)
            arr.append(s)
        for i in range(len(arr)):
            temp = temp ^ arr[i]
        return temp