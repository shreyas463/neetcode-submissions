class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}

        for i in range(len(nums)):
            current=nums[i]

            if current in hmap:
                return [hmap[current],i]
            
            needed=target-current 
            hmap[needed]=i

#so basically we started with an empty hashmap. then assigned the 1st no as current. then check if current is in hmap. if not we calculate the difference which is needed and make it the starting number. if suppose current is there in hmap, we return it along with its index value
        