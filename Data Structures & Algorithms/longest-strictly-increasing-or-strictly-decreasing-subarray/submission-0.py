class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longestIncreasing = [1]
        longestDecreasing = [1]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                longestIncreasing[-1] += 1
                longestDecreasing.append(1)
            elif nums[i-1] > nums[i]:
                longestDecreasing[-1] += 1
                longestIncreasing.append(1)
            else:
                longestIncreasing.append(1)
                longestDecreasing.append(1)
        return max(max(longestIncreasing), max(longestDecreasing))