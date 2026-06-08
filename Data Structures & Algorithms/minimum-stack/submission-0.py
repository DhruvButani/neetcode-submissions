class MinStack:

    def __init__(self):
        self.list = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.list.append(val)


        if len(self.min)==0 or val<self.min[-1]:
            self.min.append(val)

        else:
            self.min.append(self.min[-1])
        

    def pop(self) -> None:
        self.list.pop()
        self.min.pop()

        

    def top(self) -> int:
        return self.list[-1]
        

    def getMin(self) -> int:
        return self.min[-1]

        
