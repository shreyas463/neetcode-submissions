class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        ans=[0]*n

        for i in range(n):
            #if stack not empty and new temp is bgger than top of stack, we pop it
            while stack and temperatures[i]>temperatures[stack[-1]]:
                j=stack.pop() # pop the smaller one
                ans[j]=i-j #calculate the diff

            stack.append(i)
        
        return ans

        