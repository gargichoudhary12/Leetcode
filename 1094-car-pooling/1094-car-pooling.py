class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passChange = [0]*1001
        for t in trips:
            numPassengers, start, end = t
            passChange[start]+=numPassengers
            passChange[end]-=numPassengers
        curr = 0
        for i in range(1001):
            curr += passChange[i]
            if curr>capacity:
                return False
        return True
            
        