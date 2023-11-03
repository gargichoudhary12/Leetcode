class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = 0
        res=[]
        
        for i in range(1,n+1):
            if i in target:
                res.append("Push")
                ans=max(len(res),ans)
            else:
                res.append("Push")
                res.append("Pop")
        return res[:ans]  