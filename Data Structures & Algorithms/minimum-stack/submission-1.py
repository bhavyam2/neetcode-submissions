class MinStack:

    def __init__(self):
        self.stack = []
        self.currmin = []
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.currmin.append(val)
        else:
            if val <= self.currmin[-1]:
                self.currmin.append(val)
                self.stack.append(val)
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if self.currmin[-1] == self.stack[-1]:
            self.currmin.pop()
            self.stack.pop()
        else:
            self.stack.pop()
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currmin[-1]
