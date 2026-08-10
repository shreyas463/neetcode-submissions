class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x=m-1 #last real element in nums 1
        y=n-1 #last number in nums2
        z=m+n-1 #last position in nums1

        while y>=0:#until all numbers from nums2 are placed into nums1

            if x>=0 and nums1[x]> nums2[y]:
                nums1[z]=nums1[x]
                x-=1
            else:
                nums1[z]=nums2[y]
                y-=1

            z-=1


        