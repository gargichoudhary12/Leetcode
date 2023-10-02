class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        occurence = collections.Counter(nums)
        res = []
        occurence = dict(sorted(occurence.items(), key = lambda x: (x[1], -x[0])))
        for k, v in occurence.items():
            res += [k] * v
        return res