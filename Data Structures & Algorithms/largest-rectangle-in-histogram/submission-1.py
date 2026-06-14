class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxArea = 0
        for i in range(len(heights)):
            bar = heights[i]

            if(len(stack) != 0 and bar<stack[-1][1]):
                
                while(len(stack) != 0 and bar<stack[-1][1]):

                    temp = stack.pop()
                    area = temp[1] * (i-temp[0])

                    if(area>maxArea):
                        maxArea = area

                stack.append([temp[0],bar])
            
            else:
                stack.append([i,bar])
        
        for i in range(len(stack)):
            area = stack[i][1]* (len(heights)-stack[i][0])
            if(area>maxArea):
                maxArea = area


        return maxArea


            

        