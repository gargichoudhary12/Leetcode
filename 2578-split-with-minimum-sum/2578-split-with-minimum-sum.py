class Solution:
    def splitNum(self, num: int) -> int:
        a = sorted([int(i) for i in str(num)])
        b = ''
        c = ''
        for ind, x in enumerate(a):
            if ind%2 == 0:
                b += str(x)
            else:
                c += str(x)
        return int(b)+int(c)