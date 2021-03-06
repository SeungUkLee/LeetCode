class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []

    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return min(self.stk)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


