class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # idea: add value if less than target, if more, then this is a bad set, return none
        # add other value if less than target 
        # those are our two options
        # let's use dfs for this.
        

        output = []
        subset = []
        self.curr_sum = 0

        def backtrack(i):

            if self.curr_sum == target:
                output.append(subset.copy())
                return
            elif self.curr_sum > target or i >= len(nums):
                return

            

            # add the next value
            self.curr_sum += nums[i]
            subset.append(nums[i])
            backtrack(i)

            subset.pop()
            self.curr_sum -= nums[i]
            backtrack(i+1)
            
                      
            
        
        backtrack(0)

        return output