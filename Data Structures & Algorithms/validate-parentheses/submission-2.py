class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracks={ "(" : ")", "{" : "}", "[" : "]"}

        for c in s:
            if c in bracks:
                stack.append(c)
                continue
            if not stack or bracks[stack[-1]]!= c:
                return False
            stack.pop()
        return not stack
        