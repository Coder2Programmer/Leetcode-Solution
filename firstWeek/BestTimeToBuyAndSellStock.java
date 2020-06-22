class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null) {
            return 0;
        }
        
        int maxProfit = 0;
        int currentProfit = 0;
        for (int i = 1; i < prices.length; i++) {
            currentProfit = Math.max(currentProfit + prices[i] - prices[i-1], 0);
            maxProfit = Math.max(maxProfit, currentProfit);
        }
        return maxProfit;
    }
}
