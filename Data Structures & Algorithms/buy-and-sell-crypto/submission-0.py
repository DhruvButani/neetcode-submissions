class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        maxDiff = 0

        while(sell<len(prices)-1): 
            sell+=1
            diff = prices[sell] - prices[buy]
            if(diff>maxDiff):
                maxDiff = diff
                
            while(prices[sell]<prices[buy]):
                buy+=1

           
        return maxDiff
        
        