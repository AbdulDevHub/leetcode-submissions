class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for word in strs:
            sorted_key = "".join(sorted(word))
            # setdefault looks up the key; if it doesn't exist, it sets it to [] first
            anagram_map.setdefault(sorted_key, []).append(word)
            
        return list(anagram_map.values())
