class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0
        count={}
        l=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1)-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            longest=max(longest,r-l+1)
        return longest





# charset=set()
#         res=0
#         l=0
#         for r in range(len(s)):
#             while s[r] in charset:
#                 charset.remove(s[l])
#                 l+=1
#             charset.add(s[r])
#             res=max(res,r-l+1)
#         return res







      
        # res = 0  # Initialize the result to store the maximum length of the valid window
        # count = {}  # Dictionary to keep track of the frequency of characters in the current window
        # l = 0  # Left pointer of the sliding window

        # # Iterate through the string with the right pointer
        # for r in range(len(s)):
        #     # Update the count of the current character at the right pointer
        #     count[s[r]] = 1 + count.get(s[r], 0)

        #     # Check if the current window size minus the count of the most frequent character is greater than k
        #     while (r - l + 1) - max(count.values()) > k:
        #         # If so, decrement the count of the character at the left pointer
        #         count[s[l]] -= 1
        #         # Move the left pointer to the right to shrink the window
        #         l += 1

        #     # Update the result with the maximum length of the valid window
        #     res = max(res, r - l + 1)

        # return res  # Return the maximum length of the valid window

        