class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hash map for each word
        # word 1

        all_set = {}
        output = []

        for i in range(0, len(strs)):
            new_set = [0] * 26
            for j in range(0, len(strs[i])):
                new_set[ord(strs[i][j])-ord('a')] += 1

            if tuple(new_set) not in all_set:
                # figure out which one it is
                all_set[tuple(new_set)] = []
            
            all_set[tuple(new_set)].append(strs[i])
        
        for i in all_set:
            output.append(all_set[i])
        
        return output
        


            
            
        