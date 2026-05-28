class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}

        # enumerate() gives us both the index and the value instantly
        for i, current_num in enumerate(nums):
            complement = target - current_num

            # Dictionary lookups in Python are O(1) on average
            if complement in seen_numbers:
                return [seen_numbers[complement], i]

            seen_numbers[current_num] = i

        return []