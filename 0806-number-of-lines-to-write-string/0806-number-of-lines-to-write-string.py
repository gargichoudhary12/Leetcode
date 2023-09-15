class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        count_lines = 1
        current_line_width = 0

        for letter in s:
            index = ord(letter) - ord('a')
            letter_width = widths[index]
            if current_line_width + letter_width <= 100:
                current_line_width += letter_width
            else:
                count_lines += 1
                current_line_width = letter_width

        return [count_lines, current_line_width]