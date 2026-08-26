class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we use set because we dont want duplicates
        charset=set()
        l=0
        length=0

        for r in range(len(s)):
            while s[r] in charset: #if character is already present, we move l and also remove that duplicate character
                charset.remove(s[l])
                l+=1
            #we then add the new character found
            charset.add(s[r])
            length=max(length,r-l+1) 
        return length
        