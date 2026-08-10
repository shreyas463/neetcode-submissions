class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset=set() #create an empty set 
        for num in nums: #for every number in nums, we check if present in numset
            if num not in numset:
                numset.add(num)
            else:
                return True

        return False
                
        