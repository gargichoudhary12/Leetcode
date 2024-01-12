class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        vowels_count = 0
        mid_index = len(s) // 2

        for i in range(mid_index):
            char_a = s[i]
            char_b = s[mid_index + i]
            if char_a in vowels:
                vowels_count += 1
            if char_b in vowels:
                vowels_count -= 1

        return vowels_count == 0