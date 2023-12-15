class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        keys = []
        values = []
        for path in paths:
            values.append(path[1])
            keys.append(path[0])
        for value in values:
            if value not in keys:
                return value