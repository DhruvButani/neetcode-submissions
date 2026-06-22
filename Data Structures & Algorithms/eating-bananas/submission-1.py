import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        
        #noraml binary search + check on value

        while(low<=high):
            k = (low+high)//2
            hours = 0

            for i in piles:
                hours += math.ceil(i/k)

            if(hours>h):
                low = k+1

            else:
                high = k-1


        return high+1



