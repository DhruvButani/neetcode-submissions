class Solution:
    def trap(self, height: List[int]) -> int:


        #find max heights per left and right

        maxLeft = []
        maxRight = [0] * len(height)

        maxHeightLeft = 0
        maxHeightRight = 0

        for i in range(len(height)):
            maxLeft.append(maxHeightLeft)            
            maxHeightLeft = height[i] if height[i]>maxHeightLeft else maxHeightLeft

        for j in range(len(height)-1,0,-1):
            maxRight[j] = maxHeightRight
            maxHeightRight = height[j] if height[j]>maxHeightRight else maxHeightRight


        areaArr = []
        for i in range(len(height)):
            sol = min(maxLeft[i],maxRight[i])-height[i]
            areaArr.append(sol) if sol>0 else areaArr.append(0)

        return sum(areaArr)

