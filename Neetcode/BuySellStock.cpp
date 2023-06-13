class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min = 0;
        int maxprofit = 0;
        for (int i=0; i < prices.size(); i++){
            if (prices[i] < prices[min]){
                min = i;
            }
            else{
                maxprofit = max(maxprofit, prices[i] - prices[min]);
            }
        }
        return maxprofit;
    }
};
