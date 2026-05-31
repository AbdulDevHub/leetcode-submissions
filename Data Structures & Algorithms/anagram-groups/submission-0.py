class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for word in strs:
            foundAnagramClass = False
            for anagramClass in output:
                if sorted(anagramClass[0]) == sorted(word):
                    anagramClass.append(word)
                    foundAnagramClass = True
                    break
            if not foundAnagramClass: output.append([word])
        return output

        