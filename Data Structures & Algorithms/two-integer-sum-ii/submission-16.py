class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x,y=0,len(numbers)-1
        
        while x<y:
            cursum= numbers[x]+numbers[y]

            if cursum==target:
                return [x+1,y+1]

            elif cursum>target:
                y-=1

            else:
                x+=1
