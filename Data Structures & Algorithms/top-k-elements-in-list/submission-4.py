class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap=defaultdict(int)
        for num in nums:
            freqmap[num]+=1

        heap=[]
        for num, freq in freqmap.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
            
        return[num for freq, num in heap]


        