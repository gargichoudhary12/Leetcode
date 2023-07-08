class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.maxtime = 0
        self.minheap = []
        self.maxheap = []
        
        

    def update(self, timestamp: int, price: int) -> None:
        self.timestamps[timestamp]=price
        self.maxtime = max(self.maxtime, timestamp)
        heapq.heappush(self.minheap,(price,timestamp))
        heapq.heappush(self.maxheap,(-price,timestamp))
        

    def current(self) -> int:
        return self.timestamps[self.maxtime]
        

    def maximum(self) -> int:
        currprice, timestamp = heapq.heappop(self.maxheap)
        while -currprice != self.timestamps[timestamp]:
            currprice, timestamp = heapq.heappop(self.maxheap)
        heapq.heappush(self.maxheap, (currprice, timestamp))
        return -currprice
            

    def minimum(self) -> int:
        currprice, timestamp = heapq.heappop(self.minheap)
        while currprice != self.timestamps[timestamp]:
            currprice, timestamp = heapq.heappop(self.minheap)
        heapq.heappush(self.minheap, (currprice, timestamp))
        return currprice


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()