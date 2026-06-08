class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(':3,'{':2,'[':1}
        closing = {')':3,'}':2,']':1}

        for c in s:
            if c in opening:
                stack.append(opening[c])
            elif c in closing:
                if len(stack) == 0 or stack[-1] != closing[c]:
                    return False
                stack.pop()
        
        if len(stack)>0:
            return False

        return True
        
        