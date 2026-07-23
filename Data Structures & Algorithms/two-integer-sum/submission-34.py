class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={

        }
        for i in range(len(nums)):
            current = nums[i]

            if current in hmap:
                return [hmap[current],i]
            
            needed=target-current
            hmap[needed]=i


    #         class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hmap={

    #     }
    #     for i in range(len(nums)):
    #         current =nums[i] #3 , 4

    #         if current in hmap: #3 in hmap - no , 4 in map - yes
    #             return [hmap[current],i] #so return back 0 (position), i value which is 1

    #         needed=target-current #7-3=4
    #         hmap[needed]=i # 4 at 0

        

        