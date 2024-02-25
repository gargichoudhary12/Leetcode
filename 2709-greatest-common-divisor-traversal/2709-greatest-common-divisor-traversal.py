class UnionFind:
    def __init__(self, n):
        self.parent = {i:i for i in range(n)}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
            
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        if 1 in nums:
            return False

        nums = list(set(nums))
        
        n = len(nums)
        uf = UnionFind(n)
        factorMap= {}

        for i, num in enumerate(nums):
            for j in range(2, isqrt(num) + 1):
                if num % j == 0:
                    if j not in factorMap:
                        factorMap[j] = i
                    else:
                        uf.union(i, factorMap[j])
                    while num%j == 0:
                        num = num//j
            if num == 1:
                continue
            if num not in factorMap:
                factorMap[num] = i
            else:
                uf.union(i, factorMap[num])
                
        connected = set()
        for i in range(n):
            connected.add(uf.find(i))
            
        return len(connected) == 1