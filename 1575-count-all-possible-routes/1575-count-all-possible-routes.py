class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        ans = {}
        def dfs(i, total):
            if total < 0:
                return 0
            if (i, total) in ans:
                return ans[(i, total)]
            count = 0
            if i == finish:
                count += 1
            for j in range(len(locations)):
                if j != i:
                    count += dfs(j, total - abs(locations[j] - locations[i]))
            ans[(i, total)] = count
            return count
        return dfs(start, fuel) % (10 ** 9 + 7)