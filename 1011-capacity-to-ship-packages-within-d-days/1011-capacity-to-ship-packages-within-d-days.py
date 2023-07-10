class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        
        def canShip(capacity):
            ships = 1
            currCapacity = capacity
            for w in weights:
                if currCapacity-w<0:
                    ships+=1
                    currCapacity = capacity
                currCapacity-=w
            return ships<=days
        
        while l<=r:
            capacity = (l+r)//2
            if canShip(capacity):
                res = min(res, capacity)
                r = capacity-1
            else:
                l = capacity+1
        return res