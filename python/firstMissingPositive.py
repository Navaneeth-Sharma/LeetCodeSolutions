class Solution:
    def swap(self,a,b):
        return b,a
    def firstMissingPositive(self, arr: List[int]) -> int:
        i = 0
        while i<len(arr):
            correct = arr[i]-1
            
            if arr[i]<len(arr) and arr[i]>0 and arr[i]!=arr[correct]  :
                arr[i],arr[correct] = self.swap(arr[i],arr[correct])
            else:
                i+=1

        for i in range(len(arr)):
            
            if i+1!=arr[i]:
                return i+1
        return len(arr)+1