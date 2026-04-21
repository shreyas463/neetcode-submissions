class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracks = {"(": ")", "[": "]", "{": "}"}
        
        for c in s:
            if c in bracks:  # if it's an opening bracket
                stack.append(c)
            else:  # if it's a closing bracket
                if not stack or bracks[stack[-1]] != c:
                    return False
                stack.pop()
        
        return not stack
