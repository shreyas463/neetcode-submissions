class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for i in strs:
            sorted_as="".join(sorted(i))
            ans[sorted_as].append(i)
        return list(ans.values())
        