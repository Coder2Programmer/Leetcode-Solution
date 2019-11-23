class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length <= 0) {
            return -1;
        }
        
        int low = 0;
        int high = nums.length - 1;
        while (low < high) {
            int mid = (low + high) >>> 1;
            if (nums[mid] > nums[high]) {
                low = mid + 1;
                continue;
            }
            high = mid;
        }
        
        int rotatedLength = low;
        low = 0;
        high = nums.length;
        while (low < high) {
            int mid = (low + high) >>> 1;
            int realMid = (mid + rotatedLength) % nums.length;
            if (nums[realMid] < target) {
                low = mid + 1;
                continue;
            }
            high = mid;
        }
        int index = (low + rotatedLength) % nums.length;
        return nums[index] == target ? index : -1;
    }
}
