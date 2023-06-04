class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        num_provinces = 0
        for i in range(n):
            # If the city has not been visited yet
            if visited[i] == 0:
                queue = deque([i])
                visited[i] = 1
                while queue:
                    city = queue.popleft()
                    for j in range(n):
                        if isConnected[city][j] == 1 and visited[j] == 0:
                            queue.append(j)
                            visited[j] = 1
                num_provinces += 1
        return num_provinces