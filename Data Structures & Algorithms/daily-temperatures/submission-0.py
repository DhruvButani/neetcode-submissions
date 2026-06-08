class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = []
        for t in range(len(temperatures)):
            while len(stack) != 0 and temperatures[t]>temperatures[stack[-1]]:
                j = stack.pop()
                sol[j] = t-j
            stack.append(t)
        return sol
        