class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numset=set()
        
        for num in nums: #for every number in nums
            if num not in numset: #if not in nuumset, we add it
                numset.add(num) 
            else: #if there, give true
                return True
        return False
        