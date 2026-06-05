class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentsum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: currentsum += nums[i]
            else: currentsum = nums[i]
            maxSum = max(maxSum, currentsum)
        return maxSum
