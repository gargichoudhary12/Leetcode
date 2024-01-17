class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        tmp = set(arr)
        res = []
        for num in tmp:
            res.append(arr.count(num))

        return len(res) == len(set(res))