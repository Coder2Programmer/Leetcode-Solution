class Solution {
    public int trap(int[] height) {
        if (height == null || height.length <= 0) {
            return 0;
        }
        
        int waterVolumn = 0;
        int left = 0;
        int right = height.length - 1;
        int leftHighest = height[left];
        int rightHighest = height[right];
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] > leftHighest) {
                    leftHighest = height[left];
                    continue;
                }
                waterVolumn += leftHighest - height[left];
                left++;
                continue;
            }
            if (height[right] > rightHighest) {
                rightHighest = height[right];
                continue;
            }
            waterVolumn += rightHighest - height[right];
            right--;
        }
        return waterVolumn;
    }
}
