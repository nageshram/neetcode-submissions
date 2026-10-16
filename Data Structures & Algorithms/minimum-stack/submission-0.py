class MinStack:

    def __init__(self):
        self.stack = list()
        self.min = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min)== 0:
            self.min.append(val)
        elif self.min[-1]>=val:
            self.min.append(val)

    def pop(self) -> None:
        x=self.stack.pop()
        if x== self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
