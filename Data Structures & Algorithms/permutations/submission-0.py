class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # to permute we must use dfs 
        unique = set()
        permutes = []


        # we can permute the order 
        # since the numbers are unique we can use a dp instead
        # but what if it is not unique?

        def dfs(permute):
            if len(permute) == len(nums):
                permutes.append(permute.copy())
                return 
            
            for i in nums:
                if i not in permute:
                    permute.append(i)
                    dfs(permute)
                    permute.pop()


        dfs([])
        return permutes 
           