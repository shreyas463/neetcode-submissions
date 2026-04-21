from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer=defaultdict(list)
        for i in strs:
            sorted_answer="".join(sorted(i))
            answer[sorted_answer].append(i)
        return list(answer.values())
        