class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        A = Counter(arr).most_common()
        while A and k >= A[-1][1]: 
            k -= A.pop()[1]
        return len(A)