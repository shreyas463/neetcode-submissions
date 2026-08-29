class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracks={"(":")", "{":"}", "[": "]"} 

        for c in s:
            if c in bracks: #if oopen brack push into stack
                stack.append(c)
                continue
            if not stack or bracks[stack[-1]]!=c:  #if empty or current brack does not match last (top) of stk
                return False
            
            stack.pop() #matched open=close brack

        return not stack
        