class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        candidates.sort()
        def backtrack(i, subset, total):
            if total == target:
                output.append(subset.copy())
                return
            elif total > target or i >= len(candidates):
                return

            # the issue i didnt observe are the duplicate numbers
            # if there is a duplicate number, there is a chance that we get
            # a duplicate result from summing.
            # this difference between combination II and combination I 
            # when skipping, do not use the same elment
            
            subset.append(candidates[i])
            backtrack(i+1, subset, total + candidates[i])

            subset.pop()
            while ( i+1 < len(candidates) and candidates[i] == candidates[i+1]):
                i += 1
            backtrack(i+1, subset, total)
             

            
            
        backtrack(0, [], 0)        
        return output