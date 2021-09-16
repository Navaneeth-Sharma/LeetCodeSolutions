class Solution:
    def merge(self, arr1, arr2):
        i=0
        j=0
        arr = []
        while(i<len(arr1) and j<len(arr2)):
            if arr1[i]<arr2[j]:
                arr.append(arr1[i])
                i+=1
            else:
                arr.append(arr2[j])
                j+=1
        while i<len(arr1):
            arr.append(arr1[i])
            i+=1
        while j<len(arr2):
            arr.append(arr2[j])
            j+=1

        return arr 
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = self.merge(nums1, nums2)
        mid = len(arr)//2
        if len(arr)%2==0:
            return (arr[mid-1]+arr[mid])/2
        else:
            return arr[mid]