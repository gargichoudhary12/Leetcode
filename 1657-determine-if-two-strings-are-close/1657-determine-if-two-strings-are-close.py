class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        d1 = defaultdict(list)
        for c in counter1.keys():
            d1[counter1[c]].append(c)

        d2 = defaultdict(list)
        for c in counter2.keys():
            d2[counter2[c]].append(c)

        if d1.keys() != d2.keys():
            return False

        for k in d1.keys():
            if len(d1[k]) != len(d2[k]):
                return False
        return True