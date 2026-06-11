class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        a = {'(': ')',
            '[': ']',
            '{': '}'}

        b = {')': '(',
            ']': '[',
            '}': '{'}

        for i in s:
            
            if(i in a):
                stack.append(i)
            
            else:
                if(len(stack) == 0 or b[i]!= stack.pop()):
                    return False

        
        if(len(stack) != 0):
            return False

    
        return True