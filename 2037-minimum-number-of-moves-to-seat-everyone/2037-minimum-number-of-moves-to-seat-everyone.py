class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        result = 0
        for i in range(len(seats)):
            result += abs(seats[i]-students[i])
        
        return int(result)