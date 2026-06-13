class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        currCars = [[position[i],speed[i]] for i in range(len(position))]
        currCars.sort(key = lambda item: item[0])

        stack = []

        for i in reversed(currCars):

            arrivalTime = (target-i[0])/i[1]

            if(len(stack) == 0 or arrivalTime>stack[-1]):
                stack.append(arrivalTime)

        return len(stack)