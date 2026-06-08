class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        startingPoints = set()

        for i in nums:
            if i-1 not in values:
                startingPoints.add(i)
        
        maxSeq = 0
        for k in startingPoints:
            start = k
            seq = 1

            while(start+1 in values):
                seq+=1
                start+=1
                
            if seq>maxSeq:
                maxSeq = seq

        return maxSeq
        