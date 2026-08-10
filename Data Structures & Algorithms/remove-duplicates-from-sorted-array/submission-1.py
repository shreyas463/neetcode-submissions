class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l,r=0, 1

        while r<len(nums):

            if nums[l]==nums[r]:
                del nums[r]

            else:
                l+=1
                r+=1

        return len(nums) #returning the number of unique elemtns
           

        