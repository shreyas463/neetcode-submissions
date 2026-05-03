class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #defining the freqmap
        freqmap=defaultdict(int) #creating empty dict starting from 0
        for num in nums: #adding each number
            freqmap[num]+=1 #noting number and freq

#Use a min-heap to find the top k elements
        heap=[] #empty in start
        for num, freq in freqmap.items(): #key,value (d,c)(a,b)
            heapq.heappush(heap,(freq,num)) #gets stored as [(freq:no)]
            if len(heap)>k:
                heapq.heappop(heap)
        # Step 3: Extract the elements from the heap      
        return [num for freq, num in heap] #[expression for item in iterable]



        