class Solution:
    def findMin(self, nums: List[int]) -> int:
        runningMin = nums[0]
        left = 0
        right = len(nums)-1

        while(left<=right):
            mid = (left + right) // 2

            if(nums[left]<nums[right]):
                runningMin = min(runningMin, nums[left])


            runningMin = min(runningMin, nums[mid])
            if(nums[mid] >= nums[left]):
                left = mid+1
            else:
                right = mid-1


        return runningMin