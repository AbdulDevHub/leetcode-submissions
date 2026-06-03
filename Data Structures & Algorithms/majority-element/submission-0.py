class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}
        for num in nums:
            if num in countMap: countMap[num] += 1
            else: countMap[num] = 1
        return max(countMap, key=countMap.get)