class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x,y=0,len(numbers)-1

        while x<y:

            cs=numbers[x]+numbers[y]

            if cs==target:
                return [x+1,y+1]

            elif cs>target:
                y-=1
            else:
                x+=1

        