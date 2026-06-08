class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        
        a = self.findMin(nums[0:(len(nums)//2)])
        b = self.findMin(nums[len(nums)//2:])

        return min(a,b)
        