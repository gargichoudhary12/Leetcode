class Solution:
    def countLargestGroup(self, n: int) -> int:
        def cou(n):
            s=0
            while (n>0):
                s+=n%10
                n=n//10
            return s
        l=[0]*36 
        for i in range(1,n+1):
            l[cou(i)-1]+=1
        return l.count(max(l))