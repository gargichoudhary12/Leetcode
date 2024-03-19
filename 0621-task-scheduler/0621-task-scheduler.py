class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        mx = max(d.values())
        c = list(d.values()).count(mx)
        return max(len(tasks), (mx-1)*(n+1)+c)