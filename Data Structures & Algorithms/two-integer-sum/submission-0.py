class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        j = 0

        some_set = {}
        for k in range(0, len(nums)):
            some_set[nums[k]] = k 

        for k in range(0,len(nums)):
            if target - nums[k] in some_set:
                j = some_set[target-nums[k]]
                break
            
            
            

        
        return [i,j]