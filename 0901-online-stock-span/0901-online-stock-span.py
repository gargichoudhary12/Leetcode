class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        day =1
        while self.stack and self.stack[-1][0]<=price:
            day+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,day))
        return day

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)