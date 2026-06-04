class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreaterElementArray = []
        for num1 in nums1:
            num2Index = nums2.index(num1)
            nextGreaterNum = -1
            for i in range(num2Index+1, len(nums2)):
                if nums2[i] > num1: 
                    nextGreaterNum = nums2[i]
                    break
            nextGreaterElementArray.append(nextGreaterNum)
        return nextGreaterElementArray
            