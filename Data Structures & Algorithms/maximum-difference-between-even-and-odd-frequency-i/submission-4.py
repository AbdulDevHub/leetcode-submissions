class Solution:
    def maxDifference(self, s: str) -> int:
        countMap = {}
        for char in s:
            if char in countMap: countMap[char] += 1
            else: countMap[char] = 1
        evens = [x for x in countMap.values() if x % 2 == 0]
        odds = [x for x in countMap.values() if x % 2 != 0]
        return max(odds) - min(evens)        
