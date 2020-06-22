class Solution {
    public int maxArea(int[] height) {
        if (height == null) {
            return 0;
        }
        
        int left = 0;
        int right = height.length - 1;
        int mostWater = 0;
        while (left < right) {
            int currentWater = Math.min(height[left], height[right]) * (right - left);
            mostWater = Math.max(mostWater, currentWater);
            if (height[left] < height[right]) {
                left++;
                continue;
            }
            right--;
        }
        return mostWater;
    }
}
