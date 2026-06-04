class Solution:
    def maxDifference(self, s: str) -> int:
        countMap = {}
        for char in s: countMap[char] = countMap.get(char, 0) + 1
        maxOdd, minEven = -1, float("inf")
        for count in countMap.values():
            if count % 2 != 0: maxOdd = max(maxOdd, count)
            else: minEven = min(minEven, count)
        return maxOdd - minEven