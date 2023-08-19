class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda x: x[2])
        res, father, sz = [[], []], [i for i in range(n)], len(edges)

        def find_father(x):
            if father[x] != x:
                father[x] = find_father(father[x])
            return father[x]

        def union(x, y):
            x_father, y_father = find_father(x), find_father(y)
            if x_father != y_father:
                father[x_father] = y_father

        def kruskal(deleted_edge):
            total = 0
            for i in range(len(edges)):
                if i == deleted_edge:
                    continue
                if find_father(edges[i][0]) != find_father(edges[i][1]):
                    total += edges[i][2]
                    union(edges[i][0], edges[i][1])
            for i in range(n - 1):
                if find_father(i) != find_father(i + 1):
                    total = sys.maxsize
                    break
            return total

        min_sum, set1 = kruskal(-1), set()
        for i in range(sz):
            for j in range(n):
                father[j] = j
            score = kruskal(i)
            if score > min_sum:
                res[0].append(edges[i][3])
                set1.add(i)
        for i in range(sz):
            if i in set1:
                continue
            for j in range(n):
                father[j] = j
            edges.insert(0, edges[i])
            if kruskal(i + 1) == min_sum:
                res[1].append(edges[i + 1][3])
            edges.pop(0)

        return res