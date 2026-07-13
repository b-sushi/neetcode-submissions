class MinStack:

    def __init__(self):
        self.stk = []
        self.stk_min = []
    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.stk_min:
            self.stk_min.append(val)
        elif self.stk_min[-1] >= val:
            self.stk_min.append(val)
    def pop(self) -> None:
        temp = self.stk.pop()
        if self.stk_min[-1] == temp:
            self.stk_min.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.stk_min[-1]
        
