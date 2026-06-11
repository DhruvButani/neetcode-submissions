from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        freq_arr = [[] for i in range(1,2+len(nums))]
        freq_dict = Counter(nums)

        print(freq_arr)
        for value, frequency in freq_dict.items():
            freq_arr[frequency].append(value)

        
        count = len(freq_arr)-1
        i = k
        sol = []
        while(i != 0):
            i = i-len(freq_arr[count])
            sol.extend(freq_arr[count])
            count -=1
        


        return sol