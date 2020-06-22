class Solution {
    private List<String> typeList = new LinkedList<>();

    public List<String> generateParenthesis(int n) {
        helper(n, n, new StringBuilder());
        return typeList;
    }

    private void helper(int left, int right, StringBuilder sb) {
        if (left > 0) {
            helper(left - 1, right, sb.append('('));
            sb.deleteCharAt(sb.length() - 1);
        }
        if (right > left) {
            helper(left, right - 1, sb.append(')'));
            sb.deleteCharAt(sb.length() - 1);
        }
        if (left <= 0 && right <= 0) {
            typeList.add(sb.toString());
        }
    }

}