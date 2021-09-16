class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = dict()
        for i in range(len(nums)):
            try:
                d[target-nums[i]]
                return [d[target-nums[i]], i]
            except:
                d[nums[i]] = i
                
                