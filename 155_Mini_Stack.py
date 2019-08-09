class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.stack.append((x, curMin))
        
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
    
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0] if self.stack else None
    
    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1] if self.stack else None
        