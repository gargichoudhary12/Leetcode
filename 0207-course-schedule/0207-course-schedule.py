class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for (course, prereq) in prerequisites:
            graph[course].add(prereq)
        for course in range(numCourses):
            if course not in graph:
                graph[course] = set()
        
        count = 0
        no_prereqs = [course for course in graph if not len(graph[course])]
        while len(no_prereqs) and count < numCourses:
            curr = no_prereqs.pop()
            count += 1
            graph.pop(curr)
            for course in graph:
                graph[course].discard(curr)
            no_prereqs = [course for course in graph if not len(graph[course])]
        
        return count == numCourses