class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr1 = []
        for e in arr:
            if len(e) == len(set(e)):
                arr1.append(e)
                
        def dp(i,s):
            if i>=len(arr1):
                return len(s)
            t1,t2 = 0,0
            if not set(arr1[i]).intersection(s):
                t1 = dp(i+1,s|set(arr1[i]))
            t2 = dp(i+1,s)
            return max(t1,t2)
        
        return dp(0,set())