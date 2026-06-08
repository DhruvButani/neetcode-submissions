class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while(left<right):
            mid = (left+right)//2

            currTime = 0
            for i in piles:
                currTime += math.ceil(i/(mid))
                
            if(currTime<=h):
                right = mid
            
            else:
                left = mid+1

        return left

        