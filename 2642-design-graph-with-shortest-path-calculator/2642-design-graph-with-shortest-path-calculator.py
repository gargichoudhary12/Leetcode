class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.mp={k:[] for k in range(n)}
        for e in edges:
            self.mp[e[0]].append((e[1],e[2]))

    def addEdge(self, edge: List[int]) -> None:
        self.mp[edge[0]].append((edge[1],edge[2]))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        dist=[float('inf') for i in range(len(self.mp))]
        hp =[(0,node1)]
        while len(hp)>0:
            d,v =heapq.heappop(hp)
            if(v==node2):
                return int(d)
            if d> dist[v]:
                continue
            for neighbor,weight in self.mp[v]:
                if(dist[neighbor]> d+weight):
                    dist[neighbor]=d+weight
                    heapq.heappush(hp,(dist[neighbor],neighbor))
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)