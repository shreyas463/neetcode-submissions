class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        #then we check if minstack is empty or if this val is smaller than minstack's elements

        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self) -> None:
        val=self.stack.pop()
        # checking if this val is also the value in minstack, if yes then remove

        if val==self.minstack[-1]:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
