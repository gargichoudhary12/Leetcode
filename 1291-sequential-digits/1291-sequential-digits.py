class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        lowLength = len(str(low))
        highLength = len(str(high))
        for currentLength in range(lowLength, highLength + 1):
            current = ""
            for n in range(1, currentLength + 1):
                current += str(n)
            if low <= int(current) <= high:
                result.append(int(current))
            nextNumber = int(current[-1]) + 1
            while nextNumber < 10:
                current = current[1:] + str(nextNumber)
                nextNumber += 1
                if low <= int(current) <= high:
                    result.append(int(current))
        return result