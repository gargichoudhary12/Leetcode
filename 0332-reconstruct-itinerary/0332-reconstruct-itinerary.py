class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for src, dest in tickets:
            graph[src].append(dest)
        
        for key in graph:
            graph[key].sort(reverse = True)
            
        ans = []
        
        def dfs(node):
            
            while graph[node]:
                dfs(graph[node].pop())
            
            ans.append(node)
        
        dfs("JFK")
        return ans[::-1]