class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds=time//(n-1)
        steps=rounds*(n-1)
        if time<n:
            result=time+1
        elif time>n:
            if rounds%2==0:
                result=(time-steps)+1
            else:
                result=n-((time-steps)+1)+1
        else:
            result=time-1
        return result
        