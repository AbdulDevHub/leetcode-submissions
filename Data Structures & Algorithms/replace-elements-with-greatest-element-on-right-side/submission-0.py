class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            maxElement = arr[i+1]
            for j in range(i+1, len(arr)):
                maxElement = max(maxElement, arr[j]) 
            arr[i] = maxElement
        arr[-1] = -1
        return arr

        