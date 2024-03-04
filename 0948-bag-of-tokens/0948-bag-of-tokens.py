class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        points=maxPoints=0        
        i=0
        j=len(tokens)-1

        while i<=j:
            if power>=tokens[i]:
                power-=tokens[i]
                i+=1
                points+=1
                maxPoints=max(points,maxPoints)
            elif points>0:
                points-=1
                power+=tokens[j]
                j-=1
            else:
                return maxPoints
        return maxPoints