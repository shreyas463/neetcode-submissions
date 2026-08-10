class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l, r = 0, 0 #both pointers we start at beginning

        result=[]

        while l < len(word1) and r < len(word2): #while they are in range

            result.append(word1[l]) #adding characters from each string
            result.append(word2[r])

            l+=1 #moving pointers as we go on
            r+=1
# if any longer word, add the rest from that word at end
        result.append(word1[l:]) 
        result.append(word2[r:])

        return "".join(result)
        # return "".join(result)
        