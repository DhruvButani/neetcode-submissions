# from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if(len(nums) == 0):
            return 0

        vals = set(nums)

        start = min(nums)
        stop = max(nums)
        maxCount = 0
        count = 0

        for i in range(start, stop+1, 1):

            if(i in vals):
                count = 1
                while(i+1 in vals):
                    i+=1
                    count+=1

                maxCount = count if count>maxCount else maxCount
            count = 0

        return maxCount