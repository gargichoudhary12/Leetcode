from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.s = SortedList()

    def addNum(self, num: int) -> None:
        self.s.add(num)
        

    def findMedian(self) -> float:
        n = len(self.s)
        if n%2==0:
            return (self.s[n//2-1]+self.s[n//2])/2
        else:
            return self.s[n//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

       