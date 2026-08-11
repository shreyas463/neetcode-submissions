class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for I in range(k):
            temp = nums.pop()
            nums.insert(0, temp) #Put temp into nums at index 0, which is the very front.
        