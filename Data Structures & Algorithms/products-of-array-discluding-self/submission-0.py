class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1]
        n = len(nums)
        curs = nums[0]
        for i in range(1,n):
            ret.append(curs)
            curs *= nums[i]
        curs = 1
        for i in range(n-2,-1,-1):
            curs *= nums[i+1]
            ret[i] *= curs
        return ret