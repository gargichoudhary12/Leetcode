class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        TrueCount = 0
        FalseCount = 0
        count = 0
        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                TrueCount += 1
            else:
                FalseCount+=1
            while TrueCount>k and FalseCount>k:
                if answerKey[left]=='T':
                    TrueCount-=1
                else:
                    FalseCount-=1
                left+=1
            count = max(count, right-left+1)
        return count
        