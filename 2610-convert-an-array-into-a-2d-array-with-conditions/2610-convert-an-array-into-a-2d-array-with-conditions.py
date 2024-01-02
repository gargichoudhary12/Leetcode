class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = collections.Counter(nums)
        
        result = []
        while not all(val == 0 for val in freq.values()):
            sub_array = []
            for key in freq:
                if freq[key] > 0:
                    sub_array.append(key)
                    freq[key] -= 1
            result.append(sub_array)
        return result