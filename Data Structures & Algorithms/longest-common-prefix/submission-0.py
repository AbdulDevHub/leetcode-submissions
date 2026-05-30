class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        compareWord = strs[0]
        longestPrefixIndex = len(compareWord)
        for wordIndex in range(1, len(strs)):
            tempLongestPrefixIndex = 0
            smallestWordLen = min(len(compareWord), len(strs[wordIndex]))
            for charIndex in range(0, smallestWordLen):
                if compareWord[charIndex] == strs[wordIndex][charIndex]:
                    tempLongestPrefixIndex += 1
                else: break
            longestPrefixIndex = min(longestPrefixIndex, tempLongestPrefixIndex)
            tempLongestPrefixIndex = 0
        return strs[0][0:longestPrefixIndex]
                