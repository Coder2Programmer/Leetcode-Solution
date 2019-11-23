class Solution {
    public int maxSubArray(int[] nums) {
        if (nums == null || nums.length < 0) {
            return 0;
        }
        
        int maxSubarraySum = Integer.MIN_VALUE;       
        int currentSum = 0;
        for (int num : nums) {
            currentSum = Math.max(currentSum + num, num);
            maxSubarraySum = Math.max(maxSubarraySum, currentSum);
        }
        return maxSubarraySum;
    }
}