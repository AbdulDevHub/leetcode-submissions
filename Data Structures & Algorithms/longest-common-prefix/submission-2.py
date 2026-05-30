class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Take the first word as the baseline
        first_word = strs[0]
        
        for i in range(len(first_word)):
            char = first_word[i]
            # Check this character against all other words
            for word in strs[1:]:
                # If the word is too short or characters don't match, we are done
                if i == len(word) or word[i] != char:
                    return first_word[:i]
                    
        return first_word