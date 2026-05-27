class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        sCompareIndex  = 0
        for tLetter in t:
            if tLetter == s[sCompareIndex]:
                sCompareIndex  += 1
                if sCompareIndex  == len(s): return True      
        return False
