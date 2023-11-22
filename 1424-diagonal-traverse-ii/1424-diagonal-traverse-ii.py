class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        def solve(matrix):
            d = collections.defaultdict(list)
            m = len(matrix)
            if m <= 0:
                return []
            
            for i, row in enumerate(matrix):
                for j, elem in enumerate(row):
                    d[i+j].append(elem)
            
            ans = []
            for k in d:
                ans.extend(d[k][::-1])
            return ans
        
        ans = solve(nums)
        
        return ans