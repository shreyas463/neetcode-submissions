class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0

        for n in nums:
            if n-1 not in numSet:
                curr=n
                cur_length=1

                while curr+1 in numSet:
                    curr+=1
                    cur_length+=1
                
                longest=max(cur_length,longest)
        
        return longest
        