class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        subset = []
        output = []
        unique_sets = set()
        self.target = target
        def backtrack(i):
            if self.target == 0 and tuple(subset) not in unique_sets:

                output.append(subset.copy())
                unique_sets.add(tuple(subset.copy()))
                return
            elif tuple(subset) in unique_sets:
                return
            elif self.target < 0 or i >= len(candidates):
                return

            
            # add this current one
            self.target -= candidates[i]
            subset.append(candidates[i])
            backtrack(i+1)

            # skip
            self.target += candidates[i]
            subset.pop()
            backtrack(i+1)

        backtrack(0)        
        return output