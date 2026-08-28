class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)
#If minstack is empty OR the new value is smaller than or equal to the current minimum.
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self):
        val = self.stack.pop()
#we check if what we just popped is also the current min, then remove it from minstack too
        if val == self.minstack[-1]:
            self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]