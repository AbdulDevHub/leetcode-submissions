class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonMap = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for char in text:
            if char in balloonMap: balloonMap[char] += 1
        balloonMap['l'] = balloonMap['l'] // 2
        balloonMap['o'] = balloonMap['o'] // 2
        return min(balloonMap.values())