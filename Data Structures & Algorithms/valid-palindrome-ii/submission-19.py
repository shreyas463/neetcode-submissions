class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True #if already a palindrome. check s and its reverse

        for i in range(len(s)): #basically checking if not a palindrome
            news= s[:i] + s[i+1:]#making a new string. removing the index and till end
#newS = "a" + "ca"
            if news==news[::-1]: 
                return True

        return False
