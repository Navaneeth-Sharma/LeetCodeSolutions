class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        while(low<=high):
            mid = low + (high-low)//2
            if low==high:

                return mid
            if nums[mid]>nums[mid+1]:
                high = mid
            elif nums[mid]<nums[mid+1]:
                low = mid+1
        return mid