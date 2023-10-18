class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = {i:set([]) for i in range(1,n+1)}
        for s,e in relations:
            graph[e].add(s)
        
        @cache
        def dp(i):
            if not graph[i]:
                return time[i-1]
            else:
                return time[i-1] + max(dp(j) for j in graph[i])
            
        res = 0
        for i in range(1,n+1):
            res = max(res,dp(i))
        
        return res