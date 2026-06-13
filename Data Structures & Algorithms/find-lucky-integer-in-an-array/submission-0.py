class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqMap = {}
        for i in range(len(arr)):
            if arr[i] in freqMap: freqMap[arr[i]] += 1
            else: freqMap[arr[i]] = 1

        largestLuckyNum = -1
        for key in freqMap:
            if freqMap[key] == key and largestLuckyNum < key:
                largestLuckyNum = key
        return largestLuckyNum