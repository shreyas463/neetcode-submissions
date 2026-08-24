class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        l,r=0,len(height)-1
        leftmax,rightmax=0,0
        water=0

        while l<=r:

            if height[l]<=height[r]: # process the shorter left side

                if height[l]>=leftmax:
                    leftmax=height[l] #new max
                else:
                    water+=leftmax-height[l] #old max is present

                l+=1
            else:

                if height[r]>=rightmax:
                    rightmax=height[r]
                else:
                    water+=rightmax-height[r]

                r-=1

        return water
        