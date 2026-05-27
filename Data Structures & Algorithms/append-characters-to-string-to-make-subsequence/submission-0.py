class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tCompareIndex = 0
        for sLetter in s:
            if sLetter == t[tCompareIndex]:
                tCompareIndex  += 1
                if tCompareIndex  == len(t): return 0
        return len(t) - tCompareIndex