class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:  # Found a duplicate, exit early!
                return True
            seen.add(num)
        return False