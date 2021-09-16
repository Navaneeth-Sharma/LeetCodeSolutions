class Solution:
    def swap(self,a,b):
        return b,a
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
        i = 0
        while i<len(arr):
            correct = arr[i]-1
            if arr[i]!=arr[correct]:
                arr[i],arr[correct] = self.swap(arr[i],arr[correct])
            else:
                i+=1
        disappear = []
        for j in range(len(arr)):
            if arr[j]!=j+1:
                disappear.append(j+1)
        return disappear