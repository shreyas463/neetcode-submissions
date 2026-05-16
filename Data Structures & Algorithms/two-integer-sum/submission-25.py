class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={

        }

        for i in range(len(nums)): #go through each number
            if nums[i] in hmap: #if its already present then we return it
                return [hmap[nums[i]],i]
            else:
                hmap[target-nums[i]]=i