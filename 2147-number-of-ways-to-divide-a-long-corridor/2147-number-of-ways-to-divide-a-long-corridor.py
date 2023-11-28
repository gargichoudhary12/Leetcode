class Solution:
    def numberOfWays(self, corridor):
        x, y, z= 1, 0, 0
        for i in corridor:
            if i == 'S':
                x, y, z = 0, x + z, y
            else:
                x, y, z = x + z, y, z
        return z % (10**9+7) 