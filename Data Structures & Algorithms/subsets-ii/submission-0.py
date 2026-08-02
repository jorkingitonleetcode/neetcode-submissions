class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        unique = set()
        permutes = []
        def dfs(i, permute):
            if i == len(nums):
                unique.add(tuple(permute))
                return 
            permute.append(nums[i])
            dfs(i+1, permute)
            permute.pop()
            dfs(i+1, permute)
        nums.sort()
        dfs(0, [])
        return [list(s) for s in unique]