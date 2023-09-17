class Solution(object):
    def shortestPathLength(self, graph):
        n, dict1 = len(graph), defaultdict(set)

        if n == 1:
            return 0

        for i in range(n):
            for j in graph[i]:
                dict1[i].add(j)
                dict1[j].add(i)

        stack = [(i,1<<i,0) for i in range(n)]
        visited = set(stack)

        while stack:
            node,state,steps = stack.pop(0)

            if state == (1<<n)-1:
                return steps

            for neighbor in dict1[node]:
                new_state = state|(1<<neighbor)
                if (neighbor,new_state) not in visited:
                    stack.append((neighbor,new_state,steps+1))
                    visited.add((neighbor,new_state))