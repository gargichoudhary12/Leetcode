class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        TCount = 0
        FCount = 0
        count = 0
        for right in range(len(answerKey)):
            if answerKey[right]=='T':
                TCount+=1
            else:
                FCount+=1
            
            while TCount>k and FCount>k:
                if answerKey[left]=='T':
                    TCount-=1
                else:
                    FCount-=1
                left+=1
            count = max(count,right-left+1)
        return count