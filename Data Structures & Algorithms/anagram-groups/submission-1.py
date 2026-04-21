class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for i in strs:
            sorted_ans="".join(sorted(i))
            ans[sorted_ans].append(i)
        return list(ans.values())
        












         # ans = defaultdict(list)  # Create a defaultdict with list as the default factory
        # for s in strs:  # Iterate over each string in the input list
        #     sorted_str = "".join(sorted(s))  # Sort the string alphabetically and join it back to form a sorted string
        #     ans[sorted_str].append(s)  # Use the sorted string as the key and append the original string to the list
        # return list(ans.values())  # Return the lists of anagrams as a list of lists
