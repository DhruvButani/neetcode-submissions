class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while(low<=high):
            t = (low + high)//2

            if(nums[t] == target):
                return t
            
            if(nums[t]>target):
                high = t-1

            if(nums[t]<target):
                low = t+1

        
        return -1