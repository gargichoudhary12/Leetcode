class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        d = { 1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}
        def days(date):
            month, day= date.split('-')
            
            return d[int(month)]+int(day)
        arrive = max(days(arriveAlice), days(arriveBob))
        leave = min(days(leaveAlice), days(leaveBob))
        return max(leave-arrive+1,0)
        