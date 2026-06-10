class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        cleanedArr = sorted([num for row in grid for num in row])
        repeatedNum = 0
        missingNum = 0

        prevNum = 0
        for num in cleanedArr:
            if num == prevNum: repeatedNum = num
            elif num - prevNum > 1: missingNum = prevNum + 1
            prevNum = num            
        if missingNum == 0: missingNum = len(cleanedArr)
        return [repeatedNum, missingNum]