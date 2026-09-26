class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones] #used neg because python doest not supp maxheap

        heapq.heapify(stones)

        while len(stones) > 1:
            first=heapq.heappop(stones) #first bigg val
            second=heapq.heappop(stones) #second big val
            if second>first:    #since we are using neg values ex (-8,-7)
                heapq.heappush(stones, first-second)
        
        return -stones[0] if stones else 0

## means stones is not empty
#To return the real (positive) weight of the remaining stone
        