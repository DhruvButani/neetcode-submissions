# from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #store the start of each sequence

        startingSequences = {}
        values = set(nums)
        
        for i in nums:
            if i-1 not in values:
                startingSequences[i] = 1
            
        maxCount = 0


        for key, v in startingSequences.items():
            count = 1

            while(key+count in values):
                count+=1
        
            if count>maxCount:
                maxCount = count


        return maxCount

        return 0