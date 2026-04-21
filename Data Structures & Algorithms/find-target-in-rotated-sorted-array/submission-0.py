class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid
            # left sorted array
            if nums[l] <= nums[mid]:
                # make sure target is in between num[l] and nums[mid]
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right sorted array
            else:
                # make sure target is in between num[mid] and nums[r]
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1