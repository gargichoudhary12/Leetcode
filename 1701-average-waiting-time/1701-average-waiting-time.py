class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prev=0
        count=0
        n=len(customers)
        for i in range(n):
            if prev and prev>customers[i][0]:
                a=prev-customers[i][0]+customers[i][1]
                count+=a
                prev=customers[i][0]+a
            else:
                b=customers[i][0]+customers[i][1]
                count+=customers[i][1]
                prev=b
        return count/n