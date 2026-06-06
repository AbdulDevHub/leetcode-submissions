class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arrMap = {}
        for string in arr:
            if string in arrMap: arrMap[string] += 1
            else: arrMap[string] = 1
        
        kCounter = 0
        for key in arrMap:
            if arrMap[key] == 1:
                kCounter += 1
                if kCounter == k: return key
        return  ""