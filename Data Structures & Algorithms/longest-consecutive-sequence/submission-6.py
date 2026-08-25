class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we first create set of nums

        numset=set(nums)
        longest=0

        for n in nums:
            #checking if its start of sequence
            if (n-1) not in numset: #if no prev value it is the start
                length=0
                while (n+length) in numset: #then we check if n+1 value is there
                    length+=1 #means there are conseq values
                longest=max(longest,length)
        return longest

        