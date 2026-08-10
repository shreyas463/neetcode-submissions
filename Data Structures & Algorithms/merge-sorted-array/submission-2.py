class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        x = m - 1          # Points to the last actual number in nums1
        y = n - 1          # Points to the last number in nums2
        z = m + n - 1      # Points to the last available position in nums1

        # Continue until all numbers from nums2 are placed into nums1
        while y >= 0:

            # If nums1 still has numbers and nums1[x] is larger
            if x >= 0 and nums1[x] > nums2[y]:

                nums1[z] = nums1[x]   # Put nums1's larger number at position z
                x -= 1                # Move x left to the next number in nums1

            else:
                nums1[z] = nums2[y]   # Put nums2's number at position z
                y -= 1                # Move y left to the next number in nums2

            z -= 1                    # Move z left to the next available position