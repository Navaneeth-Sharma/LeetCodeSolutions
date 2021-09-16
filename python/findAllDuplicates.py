class Solution:
    def swap(self,a,b):
        return b,a
    def findDuplicates(self, arr: List[int]) -> List[int]:
        i = 0
        while i<len(arr):
            correct = arr[i]-1
            if arr[i]!=arr[correct]:
                arr[i],arr[correct] = self.swap(arr[i],arr[correct])
            else:
                i+=1
        duplicate = []
        for j in range(len(arr)):
            if j+1!=arr[j]:
                duplicate.append(arr[j])
        return duplicate