class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ret = Counter(nums)

        l = [k for k in ret.keys()]

        self.qsort(ret, l, 0, len(l)-1 )
        return l[-k:]


    def qsort(self,ret,l,low,high):
        if(low>=high):
            return

        pivot = ret[l[high]] #choose pivot as dict val

        lPoint = low #left pointer
        rPoint = high #right pointer

        while(lPoint<rPoint): 

            while(ret[l[lPoint]]<=pivot and lPoint<rPoint):
                lPoint +=1

            while(ret[l[rPoint]]>=pivot and rPoint>lPoint):
                rPoint-=1

            self.swap(l,lPoint,rPoint)
        
        self.swap(l,lPoint,high)

        self.qsort(ret,l,low,lPoint-1)
        self.qsort(ret,l,lPoint+1,high)
            



    def swap(self, l, lPoint, rPoint):
        temp = l[lPoint]
        l[lPoint] = l[rPoint]
        l[rPoint] = temp


        
        