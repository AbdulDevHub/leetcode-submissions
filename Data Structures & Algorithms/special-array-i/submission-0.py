class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        evenOrOdd = nums[0] % 2
        for i in range(1, len(nums)):
            if nums[i] % 2 == evenOrOdd: return False
            evenOrOdd = nums[i] % 2
        return True