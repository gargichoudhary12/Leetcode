import queue
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = dict()
        for i,j in edges:
            if(i not in graph):
                graph[i]=[j]
            else:
                graph[i].append(j)
            if(j not in graph):
                graph[j]=[i]
            else:
                graph[j].append(i)
     
        q = queue.Queue()
        q.put(source)
        visited=set()
        while not q.empty():
            ele = q.get()
            if(ele in visited):
                continue
            visited.add(ele)
            if(ele==destination):
                return(True)
                break
            if(ele not in graph):
                continue
            for child in graph[ele]:
                q.put(child)
        return(False)
        