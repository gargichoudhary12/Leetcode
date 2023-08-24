class Solution:
    def createSentence(self, line):
        sentence = ''
        for word, spaceCount in line:
            sentence+=word
            sentence+=' '*spaceCount
            
        return sentence
    
    def adjustSpaces(self, line, spaceLeft):
        lastSpaces = line[-1][1]
        line[-1][1] = 0
        spaceLeft +=lastSpaces
        totalWords = len(line)
        
        if totalWords == 1:
            line[0][1] = spaceLeft
            return self.createSentence(line)
        
        for i in range(totalWords-1, 0, -1):
            spaceAfterWord = spaceLeft//i
            spaceLeft-=spaceAfterWord
            
            line[i-1][1] += spaceAfterWord
            
        return self.createSentence(line)    
        
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        cUsage = 0
        output = []
        for word in words:
            if cUsage + len(word) > maxWidth:
                output.append(self.adjustSpaces(line, maxWidth-cUsage))
                cUsage = len(word)+1
                line = [[word,1]]
                
            elif cUsage + len(word) == maxWidth:
                line.append([word,0])
                cUsage = maxWidth
                
            else:
                line.append([word,1])
                cUsage+=len(word)+1
                
        line[-1][1] += maxWidth - cUsage
        output.append(self.createSentence(line))
                
        return output