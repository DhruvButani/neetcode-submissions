class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops = set(['+','-','*','/'])
        stack = []

        for n in tokens:
            if(n not in ops):
                stack.append(n)
            else:
                if(n == '+'):
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a+b)
                    
                elif(n == '-'):
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b-a)
                
                elif(n == '*'):
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a*b)
            
                elif(n == '/'):
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b/a)

        return int(stack.pop())
                    

