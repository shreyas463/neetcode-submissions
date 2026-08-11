class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l,r=0,len(people)-1
        boatcnt=0

        while l<=r:
            if people[l]+people[r]>limit: #bigger than weight limit, move pointer sm
                r-=1
            else: #within range, keep moving both pointers and increase count of boats
                l+=1
                r-=1

            boatcnt+=1

        return boatcnt

        