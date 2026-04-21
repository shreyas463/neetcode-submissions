class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans=defaultdict(list) #using a empty hashmap to return like a list of strings

        for i in strs:
            sorted_answer="".join(sorted(i))
            ans[sorted_answer].append(i)

        return list(ans.values())
        