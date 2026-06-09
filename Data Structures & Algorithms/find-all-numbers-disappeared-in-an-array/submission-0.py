class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(1, len(nums)+1):
            if not i in nums: output.append(i)
        return output