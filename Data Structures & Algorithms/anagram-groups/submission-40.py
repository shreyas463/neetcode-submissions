class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for i in strs:
            sortedans="".join(sorted(i))
            ans[sortedans].append(i)
        return list(ans.values())

        