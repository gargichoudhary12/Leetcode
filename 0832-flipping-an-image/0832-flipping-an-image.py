class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            start = 0
            end = len(i) - 1
            while start <= end:
                i[start], i[end] = i[end], i[start]
                if i[start] == 1:
                    i[start] = 0
                else:
                    i[start] = 1
                if start != end:
                    if i[end] == 1:
                        i[end] = 0
                    else:
                        i[end] = 1
                start += 1
                end -= 1
        return image