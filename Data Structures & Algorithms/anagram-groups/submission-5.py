class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans=defaultdict(list)

        for i in strs:
            sorted_ans="".join(sorted(i))
            ans[sorted_ans].append(i)

        return list(ans.values())

        