class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<r:

            while l<r and not s[l].isalnum(): #char at l is not alphanumeric move-on
                l+=1
            
            while l<r and not s[r].isalnum():
                r-=1
            
            if s[l].lower()!=s[r].lower(): #both char not same then false
                return False

            l+=1 #keep continuing
            r-=1

        return True 
        