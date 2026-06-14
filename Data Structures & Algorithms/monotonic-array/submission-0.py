class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monotonic = True

        for i in range(len(nums)-1):
            if not nums[i] <= nums[i+1]: monotonic = False
        
        if not monotonic:
            monotonic = True
            for i in range(len(nums)-1):
                if not nums[i] >= nums[i+1]: monotonic = False

        return monotonic