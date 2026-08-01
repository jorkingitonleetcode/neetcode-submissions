class Solution:
    def minWindow(self, s: str, t: str) -> str:
        total = 0
        # maybe set it up here 
        new_set = {}
        for i in t:
            total += 1
            if i not in new_set:
                new_set[i] = 0
            
            new_set[i] += 1

        
        minstr = ""
        
        
        for i in range(0,len(s)):
            curr = total
            current_set = new_set.copy()
            substr = ""
            for j in range(i, len(s)):
                if s[j] in current_set and current_set[s[j]] > 0:
                    curr -= 1
                    current_set[s[j]] -= 1
                substr += s[j]
                if s[j] not in current_set and curr == total:
                    break
                if curr <= 0:
                    break 
                
            if curr == 0 and len(substr) > 0 and (len(minstr) > len(substr) or len(minstr) == 0):
                minstr = substr
        return minstr 