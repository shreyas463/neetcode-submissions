class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp=nums.pop() #pops from end
            nums.insert(0,temp) #adss the popped element at zero place
       