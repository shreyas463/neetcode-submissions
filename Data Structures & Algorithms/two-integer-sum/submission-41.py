class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}

        for i in range(len(nums)):
            current=nums[i]

            if current in hmap:
                return [hmap[nums[i]],i]

            needed=target-current
            hmap[needed]=i
        