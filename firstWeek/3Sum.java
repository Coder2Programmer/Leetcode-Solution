class Solution {
    private List<List<Integer>> threeElements = new ArrayList<>();
    
    
    public List<List<Integer>> threeSum(int[] nums) {
        if (nums == null) {
            return threeElements;
        }
        
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i-1] == nums[i]) {
                continue;
            }
            twoSum(nums, -nums[i], i + 1);
        }
        return threeElements;
    }
    
    
    private void twoSum(int[] nums, int target, int startIndex) {
        int endIndex = nums.length - 1;
        
        while (startIndex < endIndex) {
            int sum = nums[startIndex] + nums[endIndex];
            
            if (sum < target) {
                startIndex++;
                continue;
            }
            
            if (sum > target) {
                endIndex--;
                continue;
            }
            
            threeElements.add(Arrays.asList(-target, nums[startIndex], nums[endIndex]));
            do {
                startIndex++;
            } while (startIndex < endIndex && nums[startIndex-1] == nums[startIndex]);
            do {
                endIndex--;
            } while (startIndex < endIndex && nums[endIndex] == nums[endIndex+1]);
        }
    }
}