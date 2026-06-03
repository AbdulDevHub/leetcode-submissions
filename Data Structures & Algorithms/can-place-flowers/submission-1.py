class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        needToPlant = n
        lastIndex = len(flowerbed) - 1
        
        while needToPlant > 0 and lastIndex > -1:
            if flowerbed[lastIndex] == 0:
                left_empty = (lastIndex == 0) or (flowerbed[lastIndex - 1] == 0)
                right_empty = (lastIndex == len(flowerbed) - 1) or (flowerbed[lastIndex + 1] == 0)
                
                if left_empty and right_empty:
                    needToPlant -= 1
                    flowerbed[lastIndex] = 1
                    
            lastIndex -= 1
        return needToPlant <= 0
