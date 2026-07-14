class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #building map
   #  frequency map
        freqmap=defaultdict(int)
        for num in nums:
            freqmap[num] +=1
 #2) min-heap of size k storing (freq, num)
        heap=[]
        for num,freq in freqmap.items():
            heapq.heappush(heap, (freq,num))

            if len(heap)>k:#as its a min heap we are removing the least freq elements
                heapq.heappop(heap)
        
        return [num for freq, num in heap] #we storing (fre:num) we only want num

        