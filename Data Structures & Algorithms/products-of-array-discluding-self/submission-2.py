class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        pre.append(None)
        suf = [None] * len(nums)


        #iter 1 -> store each prefix 
        for i in range(1,len(nums)):
            if(pre[i-1] is None):
                pre.append(nums[i-1])
                continue
            pre.append(pre[i-1]*nums[i-1])

        for i in range(len(nums)-2, -1, -1):
            if(suf[i+1] is None):
                suf[i] = nums[i+1]
                continue 
            suf[i] = suf[i+1]*nums[i+1]

        sol = []
        sol.append(suf[0])
        for i in range(1,len(pre)-1):
            sol.append(pre[i]*suf[i])

        sol.append(pre[len(nums)-1])
        return sol