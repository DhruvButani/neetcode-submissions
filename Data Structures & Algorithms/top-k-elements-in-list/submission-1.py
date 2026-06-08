class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictionary = Counter(nums)
        freq = [[] for j in range(len(nums)+1)]
 
        
        for key, value in dictionary.items():
            freq[value].append(key)
        
        ret = []
        i = len(nums)-1
        while(len(ret)<k):
            ret.extend(freq[i])
            i-=1
        
        return ret
