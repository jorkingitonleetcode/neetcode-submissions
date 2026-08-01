class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        j = 0

        some_set = {}
        for k in range(0, len(nums)):
            some_set[nums[k]] = k 

        for k in range(0,len(nums)):
            diff = target - nums[k]
            if diff in some_set:
                i = k 
                j = some_set[diff]
                if i != j:
                    break
            
            
            

        
        return [i,j]