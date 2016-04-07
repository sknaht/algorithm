class MinStack:

    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.data = []
        self.minpos = []

    def push(self, x):
        if not self.data or x < self.data[self.minpos[-1]]:
            self.minpos.append(len(self.data))
        self.data.append(x)

    # @return nothing
    def pop(self):
        if self.minpos and len(self.data) - 1 == self.minpos[-1]:
            self.minpos.pop()
        if self.data:
            self.data.pop()

    # @return an integer
    def top(self):
        if self.data:
            return self.data[-1]

    # @return an integer
    def getMin(self):
        if self.data:
            return self.data[self.minpos[-1]]


t = MinStack()
t.push(-2)
t.push(0)
t.push(-1)
print t.getMin()
t.pop()
print t.top()
t.pop()
print t.getMin()