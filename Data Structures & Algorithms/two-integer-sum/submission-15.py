class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for x in range(len(nums)):
        #     for y in range(len(nums)):
        #         if nums[x]+nums[y]==target and x != y:
        #             return [x,y]
        hmap={}
        for i in range(len(nums)):
            if nums[i] in hmap:
                return [hmap[nums[i]],i]
            else:
                hmap[target-nums[i]]=i


        