class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack:
            if val == self.minStack[-1]:
                minVal = val
            elif val < self.minStack[-1]:
                minVal = val
            else:
                minVal = self.minStack[-1]
        else:
            minVal = val
       # minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
