class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        dict1, res = Counter(s), []

        while dict1["1"] > 1:
            res.append("1")
            dict1["1"] -= 1 
            
        while dict1["0"] > 0:
            res.append("0")
            dict1["0"] -= 1

        return "".join(res+["1"])