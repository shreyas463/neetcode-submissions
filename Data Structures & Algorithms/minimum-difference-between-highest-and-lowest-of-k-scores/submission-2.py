class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_score=float('inf') #assing a value

        n=len(nums)

        for l in range(n-k+1): #gives range-01,2,3
            r=l+k-1 ##starting index + number of elements - 1
            diff=nums[r]-nums[l]

            min_score=min(diff,min_score)

        return min_score
        