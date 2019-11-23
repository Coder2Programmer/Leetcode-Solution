class Solution {
    public void nextPermutation(int[] nums) {
        if (nums == null) {
            return;
        }

        int startIndex = nums.length - 2;
        int endIndex = nums.length - 1;
        while (startIndex >= 0 && nums[startIndex] >= nums[startIndex+1]) {
            startIndex--;
        }
        
        if (startIndex < 0) {
            reverseArray(nums, 0, endIndex);
            return;
        }
        
        while (nums[endIndex] <= nums[startIndex]) {
            endIndex--;
        }
        nums[startIndex] ^= nums[endIndex];
        nums[endIndex] ^= nums[startIndex];
        nums[startIndex] ^= nums[endIndex];
        reverseArray(nums, startIndex + 1, nums.length - 1);
    }
    
    
    private void reverseArray(int[] nums, int start, int end) {
        while (start < end) {
            nums[start] ^= nums[end];
            nums[end] ^= nums[start];
            nums[start] ^= nums[end];
            start++;
            end--;
        }
    }
}
