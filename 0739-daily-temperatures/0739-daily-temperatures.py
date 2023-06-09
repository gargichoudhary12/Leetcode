class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)        
        for i in range(len(temperatures)):
            current = temperatures[i]
            while (stack and stack[-1][0] < current):
                index = stack.pop()[1]
                ans[index] = i - index
            stack.append([current, i])
        return ans