class Solution {
    public int[] twoSum(int[] nums, int target) {
        if (nums == null || nums.length < 2) {
            return null;
        }
        
        Map<Integer, Integer> numberIndexMap = new HashMap<>();
        for (int index = 0; index < nums.length; index++) {
            int num = nums[index];
            if (numberIndexMap.containsKey(num)) {
                return new int[] {numberIndexMap.get(num), index};
            }
            numberIndexMap.put(target - num, index);
        }
        return null;
    }
}
