class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap=defaultdict(int) #creating empty dict starting from 0
        for num in nums: #adding each number
            freqmap[num]+=1 #noting number and freq


        heap=[] #empty in start
        for num, freq in freqmap.items(): #key,value (d,c)(a,b)
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
            
        return [num for freq, num in heap]


        