class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        l = 0
        r = len(people)-1
        while l<=r:
            remaining = limit-people[r]
            r-=1
            count+=1
            if l<=r and remaining>=people[l]:
                l+=1
        return count