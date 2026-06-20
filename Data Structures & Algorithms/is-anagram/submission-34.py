class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #prerequisites are lenght of two strings must be equal and indiv char too

        if len(s)!= len(t):
            return False
        
        for i in s: #going through each char cnt in strings
            if s.count(i)!=t.count(i):
                return False
        return True
        