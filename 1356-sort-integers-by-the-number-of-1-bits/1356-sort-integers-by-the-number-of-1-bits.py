class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return (sorted(arr, key = lambda x: [sum([1 for num in bin(x) if num=='1']),x]))