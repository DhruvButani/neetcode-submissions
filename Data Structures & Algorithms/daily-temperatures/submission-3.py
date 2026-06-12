class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        sol = [0] * len(temperatures)

        for index in range(len(temperatures)):


            if(len(stack)==0):
                stack.append(index)
                continue
   
            i = len(stack)-1
            while(i>=0):
                if(temperatures[stack[i]]<temperatures[index]):
                    sol[stack[i]] = index-stack[i]
                    stack.pop()
                i-=1


            stack.append(index)
            
        

        return sol
            
        