class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k%=len(nums)

        nums[:]= nums[-k:]+nums[:-k] 

        #takes all -k from plus all elements before -k
        