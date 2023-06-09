class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans=[]
        count=0
        n=len(letters)
        for i in range(0,n):
            if letters[i]>target:
                ans.append(letters[i])
                break
            else:
                count+=1
                continue
        if count==n:
            return letters[0]
        else:
            return ans[0]                