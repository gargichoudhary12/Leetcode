class Solution:
    def makeGood(self,s:str) -> str:
        # recursion
        for i in range(len(s)-1):
            if s[i]!=s[i+1] and s[i].lower()==s[i+1].lower():
                return self.makeGood(s[:i]+s[i+2::])
        return s
    
    def makeGood(self, s: str) -> str:
        # iteration
        if not s:
            return s
        stack = [s[0]]
        for i in s[1::]:
            if not stack:
                stack.append(i)
            else:
                if stack[-1]!= i and stack[-1].lower() == i.lower():
                    stack.pop()
                else:
                    stack.append(i)
        return ''.join(stack)