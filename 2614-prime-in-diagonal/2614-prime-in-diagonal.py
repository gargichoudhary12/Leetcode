class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def prime(num):
            s = set()
            for i in range(1, int(math.sqrt(num))+1):
                if num % i == 0:
                    s.add(i)
                    s.add(num//i)
            if len(s) == 2:
                return True
            else:
                return False
        l = len(nums)
        p = set([nums[i][i] for i in range(l)] + [nums[i][l-1-i] for i in range(l)])
        res = 0
        for n in p:
            if prime(n):
                res = max(res, n)
        return res