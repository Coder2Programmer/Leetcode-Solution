class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) {
            return root;
        }
        
        TreeNode leftNode = lowestCommonAncestor(root.left, p, q);
        TreeNode rightNode = lowestCommonAncestor(root.right, p, q);
        return leftNode == null ? rightNode : rightNode == null ? leftNode : root;
    }
}

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Stack<TreeNode> stack = new Stack<>();
        Map<TreeNode, TreeNode> parentNode = new HashMap<>();
        stack.push(root);
        parentNode.put(root, null);
        
        while (!parentNode.containsKey(p) || !parentNode.containsKey(q)) {
            TreeNode node = stack.pop();
            if (node.right != null) {
                stack.push(node.right);
                parentNode.put(node.right, node);
            }
            if (node.left != null) {
                stack.push(node.left);
                parentNode.put(node.left, node);
            }
        }
        
        Set<TreeNode> ancestorSet = new HashSet<>();
        while (p != null) {
            ancestorSet.add(p);
            p = parentNode.get(p);
        }
        while (!ancestorSet.contains(q)) {
            q = parentNode.get(q);
        }
        
        return q;
    }
}
