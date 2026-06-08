class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):

            #search
            left = i
            right = len(numbers)

            val = target-numbers[i]

            while(left<right):
                mid = (left+right)//2

                if(numbers[mid]<=val):
                    left = mid+1

                else:
                    right=mid
            
            if numbers[left-1] == val:
                return [i+1,left]
            

        