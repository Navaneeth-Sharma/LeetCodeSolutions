class Solution:
    def swap(self,a,b):
        return b,a
    def missingNumber(self, arr: List[int]) -> int:
        i = 0
        while i<len(arr):
            correct = arr[i]
            if arr[i]<len(arr) and arr[i]!=arr[correct]:
                arr[i],arr[correct] = self.swap(arr[i],arr[correct])
            else:
                i+=1
        for i in range(len(arr)):
            if i!=arr[i]:
                return i
        return len(arr)