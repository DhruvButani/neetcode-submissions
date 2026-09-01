class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0;
        int right = 1;
        int maxPrice = 0;

        while(right < prices.size()) {
            if(prices[left] < prices[right]) {
                maxPrice = max(prices[right] - prices[left], maxPrice);
            }
            
            else {
                left = right;
            }
            
            right +=1;
        }

        return maxPrice;
    }
};
