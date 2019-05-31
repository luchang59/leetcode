class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxStack = []
        self.helpStack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxStack or self.maxStack[-1] <= x:
            self.maxStack.append(x)

    def pop(self) -> int:
        node = self.stack.pop()
        if self.maxStack[-1] == node:
            return self.maxStack.pop()
        return node

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def peekMax(self) -> int:
        if self.maxStack:
            return self.maxStack[-1]
        return None

    def popMax(self) -> int:
        if not self.maxStack: return None
        maxValue = self.maxStack.pop()
        while self.stack:
            node = self.stack.pop()
            if node == maxValue:
                while self.helpStack:
                    self.push(self.helpStack.pop())
                return node
            self.helpStack.append(node)
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()