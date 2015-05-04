#!/user/bin/python

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0 or self.min_stack[-1][0] > x:
            self.min_stack.append((x, 1))
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1] = (x, self.min_stack[-1][1] + 1)

    # @return nothing
    def pop(self):
        p = self.stack.pop()
        if p == self.min_stack[-1][0]:
            if self.min_stack[-1][1] > 1:
                self.min_stack[-1] = (self.min_stack[-1][0], self.min_stack[-1][1] - 1)
            else:
                self.min_stack.pop()


    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.min_stack[-1][0]
