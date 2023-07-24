class Solution:
    def grayCode(self, n: int) -> List[int]:
        s = [0,1]
        m = 1
        for i in range(1,n):
            res = []
            m = m<<1
            for j in s:
                res.append(m+j)
            s+=res[::-1]
        return s