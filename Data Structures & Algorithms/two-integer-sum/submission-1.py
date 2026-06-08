class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            search = target-nums[i]
            if search in d:
                return [d[search],i]
            d[nums[i]] = i


        




        