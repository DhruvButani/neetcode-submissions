class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mydict = {}

        solArr = []

        for i in range(len(nums)):
            mydict[nums[i]] = i
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue

                value = 0-(nums[i]+nums[j])
   
                if(value in mydict and mydict[value] != i and mydict[value] != j):
                    solArr.append((nums[i],nums[j],value))
        

        # print(type(solArr[0]))
        myset = set()
        for i in solArr:
            temp = tuple(sorted(i))
            myset.add(temp)
            
        myarr = []
        for i in myset:
            myarr.append(list(i))

        return myarr

