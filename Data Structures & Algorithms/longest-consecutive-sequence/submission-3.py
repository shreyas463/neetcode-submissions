class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0

        for n in nums:
            if (n-1) not in numSet:
                curr=n
                curr_length=1

                while curr+1 in numSet:
                    curr+=1
                    curr_length+=1
                longest=max(longest,curr_length)
        return longest
            
        