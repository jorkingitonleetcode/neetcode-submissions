class Solution:
    def isValid(self, s: str) -> bool:
        # last known
        stack = []
        for c in s:
            # start with left 
            if c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif c == '(':
                stack.append(')')
            else:
                if stack[-1] == c:
                    stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False
           