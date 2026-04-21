class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmp={

        }
        for i in range(len(nums)):
            if nums[i] in hmp:
                return [hmp[nums[i]],i]
            else:
                hmp[target-nums[i]]=i

        