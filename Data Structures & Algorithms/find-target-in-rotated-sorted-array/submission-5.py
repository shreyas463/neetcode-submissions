class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        # Step 1: Find the pivot
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # Step 2: Binary search with the pivot adjustment
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            realMid = (mid + pivot) % len(nums)
            if nums[realMid] == target:
                return realMid
            if nums[realMid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
