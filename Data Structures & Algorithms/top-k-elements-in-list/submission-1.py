from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #building frequency map

        freq_map=defaultdict(int)
        for num in nums:
            freq_map[num]+=1
        
        #using min heap to find top k frequent elements

        heap=[]
        for num, freq in freq_map.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return[num for freq, num in heap]
        