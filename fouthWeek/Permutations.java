class Solution {
    List<List<Integer>> result = new LinkedList<>();

    public List<List<Integer>> permute(int[] nums) {
        List<Integer> numList = new ArrayList<>();
        for (int num : nums) {
            numList.add(num);
        }
        backtracking(numList, 0);
        return result;
    }

    private void backtracking(List<Integer> numList, int index) {
        if (index >= numList.size()) {
            result.add(new ArrayList<>(numList));
            return;
        }

        for (int i = index; i < numList.size(); i++) {
            Collections.swap(numList, index, i);
            backtracking(numList, index + 1);
            Collections.swap(numList, index, i);
        }
    }
}