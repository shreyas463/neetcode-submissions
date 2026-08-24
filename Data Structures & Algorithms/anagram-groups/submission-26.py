class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans= defaultdict(list) #using an empty hashmapt to return list of strgs at o/p

        for i in strs:
            sorted_ans="".join(sorted(i))
            ans[sorted_ans].append(i)

        return list(ans.values()) #"aet": ["eat", "tea", "ate"],

       #first sorted(i) will make eat -> a,e,t THEN "".join -> "aet" 
       #ans[aet].append(eat) using sorted word as key to compare
        