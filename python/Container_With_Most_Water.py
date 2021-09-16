class Solution:
    def maxArea(self, arr: List[int]) -> int:
        low = 0
        high = len(arr)-1
        Area = 0
        while low<high:
            Area = max(Area,(high-low)*min(arr[low],arr[high]))
            if arr[low]<arr[high]:
                low+=1
            else:
                high-=1
        return Area