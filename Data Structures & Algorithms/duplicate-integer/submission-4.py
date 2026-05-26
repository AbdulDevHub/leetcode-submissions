class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # If the length of the set is smaller than the list, duplicates exist
        return len(nums) != len(set(nums))