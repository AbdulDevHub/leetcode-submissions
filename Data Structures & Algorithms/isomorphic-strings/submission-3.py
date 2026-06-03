class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        characterMapS = {}
        characterMapT = {}
        for i in range(len(s)):
            if s[i] not in characterMapS:
                characterMapS[s[i]] = t[i]
            elif characterMapS[s[i]] != t[i]: return False
        for i in range(len(t)):
            if t[i] not in characterMapT:
                characterMapT[t[i]] = s[i]
            elif characterMapT[t[i]] != s[i]: return False
        return True