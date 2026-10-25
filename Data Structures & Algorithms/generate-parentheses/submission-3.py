class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]

        def backtract(openN,closedN):
            if openN==closedN==n:
                res.append("".join(stack))
                return
            
            if openN<n:
                stack.append("(")
                backtract(openN+1,closedN)
                stack.pop()
            
            if closedN<openN:
                stack.append(")")
                backtract(openN,closedN+1)
                stack.pop()
        
        backtract(0,0)
        return res
        