class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hash_table = [0] * 26
        for i in s:
            hash_table[ord(i) - ord("a")] += 1
        
        for i in t:
            hash_table[ord(i) - ord("a")] -= 1

        count = 0
        for i in hash_table:
            count += abs(i)

        
        return count // 2