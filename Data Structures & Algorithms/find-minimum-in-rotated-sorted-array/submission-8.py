class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2

            if nums[mid]>nums[r]:
                l=mid+1 #it means left side sorted and ele must be in right side
            else:
                r=mid #minimum element can in left side or at mid


        return nums[r] # terminates when l==r
        

	#