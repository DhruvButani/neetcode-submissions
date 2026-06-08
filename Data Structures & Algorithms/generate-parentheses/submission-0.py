class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solArr = []
        solStack = ['(']
        while(len(solStack) != 0):
            curr = solStack.pop()
            solStack.append(curr+'(')
            solStack.append(curr+')')

            i = len(solStack)-1
            while(i>=0 and len(solStack[i]) == 2*n):
                solArr.append(solStack.pop())
                i -=1
            
        ret = []

        for s in solArr:
            if self.validate(s) == True:
                
                ret.append(s)

        return ret


    def validate(self, string):

        temp = []
        for s in string:
            if s == ')':
                if len(temp) == 0:
                    return False
                else:
                    temp.pop()
            else:
                temp.append('(')


        if(len(temp) != 0):
            return False
        
        return True


        
        