class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        temp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        for i in range(len(alphabet)):
            d[alphabet[i]] = temp[i]
        transformations = []
        for word in words:
            trans = ''
            for char in word:
                trans += d[char]
            if trans not in transformations:
                transformations.append(trans)
        return len(transformations)