class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sorted_words = sorted(words, key=len)
        substringWords = []
        for firstCompare in range(len(sorted_words)):
            for secondComapare in range (firstCompare+1, len(sorted_words)):
                if sorted_words[firstCompare] in sorted_words[secondComapare]:
                    substringWords.append(sorted_words[firstCompare])
        return list(set(substringWords))