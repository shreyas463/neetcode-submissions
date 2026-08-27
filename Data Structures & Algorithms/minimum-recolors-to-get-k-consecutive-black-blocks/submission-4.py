class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        recolor=0
        result=float('inf')

        for r in range(len(blocks)):
            #if white is there, we simply increase count of recolor

            if blocks[r]=="W":
                recolor+=1
            
            #if size k reaceded-begin sliding window

            if r-l+1==k:
                result=min(recolor,result)
            
                #also we now we slide the window so remove the first char at 'l'which could be White
                if blocks[l]=="W":
                    recolor-=1
                l+=1 #moving l when size is reached and sliding window
        return result
            
        