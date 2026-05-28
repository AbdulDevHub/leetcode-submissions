class Solution:
    def scoreOfString(self, s: str) -> int:
        previousLetterValue = ord(s[0])
        stringSum = 0
        for i in range(1, len(s)):
            stringSum += abs(ord(s[i]) - previousLetterValue)
            previousLetterValue = ord(s[i])
        return stringSum