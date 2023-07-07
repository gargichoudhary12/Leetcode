class FrontMiddleBackQueue:

    def __init__(self):
        self.A = []
        

    def pushFront(self, val: int) -> None:
        self.A.insert(0,val)

    def pushMiddle(self, val: int) -> None:
        self.A.insert(len(self.A) // 2, val)
        

    def pushBack(self, val: int) -> None:
        self.A.append(val)

    def popFront(self) -> int:
        return (self.A or [-1]).pop(0)

    def popMiddle(self) -> int:
        return (self.A or [-1]).pop((len(self.A) - 1) // 2)

    def popBack(self) -> int:
        return (self.A or [-1]).pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

        

        
