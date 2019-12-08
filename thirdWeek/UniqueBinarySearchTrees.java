class Solution {
    public List<TreeNode> generateTrees(int n) {
        return n <= 0 ? new LinkedList<>() : helper(1, n);
    }
    
    private List<TreeNode> helper(int start, int end) {
        List<TreeNode> treeList = new LinkedList<>();
        for (int rootValue = start; rootValue <= end; rootValue++) {
            for (TreeNode leftChild : helper(start, rootValue - 1)) {
                for (TreeNode rightChild : helper(rootValue + 1, end)) {
                    TreeNode root = new TreeNode(rootValue);
                    root.left = leftChild;
                    root.right = rightChild;
                    treeList.add(root);
                }
            }
        }
        
        if (treeList.isEmpty()) {
            treeList.add(null);
        }
        return treeList;
    }
}
