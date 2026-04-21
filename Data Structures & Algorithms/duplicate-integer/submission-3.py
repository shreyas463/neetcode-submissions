class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset =set() #create an empty set
        for num in nums: #for every number in nums, we see if its not present in set
            if num not in numset:
                numset.add(num) #if not present we add it
            else:
                return True
        return False

        