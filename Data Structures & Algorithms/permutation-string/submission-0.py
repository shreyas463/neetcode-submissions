class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for p in permutations(s1):
            if "".join(p) in s2:
                return True
        return False
        