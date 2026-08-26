class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        min_score = float('inf')

        for l in range(n-k+1):
            #starting index + number of elements - 1
            r=l+k-1

            diff=nums[r]-nums[l]

            min_score=min(diff, min_score)

        return min_score





        