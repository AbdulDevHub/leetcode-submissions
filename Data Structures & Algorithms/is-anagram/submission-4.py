class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sorts both strings and compares them
        return sorted(s) == sorted(t)