class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(x):
            if x==1:
                return False
            for i in range(2, x//2+1):
                if x%i==0:
                    return False
            return True
        count = 0
        for i in range(1, n+1):
            if isPrime(i)==True:
                count+=1
        def factorial(y):
            fact = 1
            while y > 0:
                fact = (fact*y)%(10**9+7)
                y-=1
            return fact
        return factorial(n-count)*factorial(count)%(10**9+7)