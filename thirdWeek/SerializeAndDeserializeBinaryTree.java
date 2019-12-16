public class Codec {
    
  public String serialize(TreeNode root) {      
      StringBuilder sb = new StringBuilder();
      Stack<TreeNode> stack = new Stack<>();
      TreeNode node = root;
      
      while (!stack.isEmpty() || node != null) {
          if (node != null) {
              sb.append(Integer.valueOf(node.val)).append(" ");
              stack.push(node);
              node = node.left;
          } else {
              sb.append("# ");
              node = stack.pop();
              node = node.right;
          }
      }
      
      return sb.toString();
  }

  public TreeNode deserialize(String data) {
      if (data == null || data.length() <= 0) {
          return null;
      }
      
      String[] nodeValue = data.split(" ");
      
      TreeNode root = new TreeNode(Integer.valueOf(nodeValue[0]));
      TreeNode node = root;
      Stack<TreeNode> stack = new Stack<>();
      stack.push(node);
      
      int nodeNumber = nodeValue.length;
      int index = 1;
      while (index < nodeNumber) {
          while (index < nodeNumber && !nodeValue[index].equals("#")) {
              node.left = new TreeNode(Integer.valueOf(nodeValue[index++]));
              node = node.left;
              stack.push(node);
          }
          while (index < nodeNumber && nodeValue[index].equals("#")) {
              node = stack.pop();
              index++;
          }
          if (index < nodeNumber) {
              node.right = new TreeNode(Integer.valueOf(nodeValue[index++]));
              node = node.right;
              stack.push(node);
          }
      }
      
      return root;
  }

}


public class Codec {

  public String serialize(TreeNode root) {      
      Queue<TreeNode> queue = new LinkedList<>();
      StringBuilder sb = new StringBuilder();
      queue.offer(root);
      while (!queue.isEmpty()) {
          TreeNode node = queue.poll();
          if (node == null) {
              sb.append("# ");
          } else {
              sb.append(node.val).append(" ");
              queue.offer(node.left);
              queue.offer(node.right);
          }
      }
      
      return sb.toString();
  }

  public TreeNode deserialize(String data) {
      if (data == null || data.length() <= 0) {
          return null;
      }
      
      Queue<TreeNode> queue = new LinkedList<>();
      String[] nodeValues = data.split(" ");
      TreeNode root = new TreeNode(Integer.valueOf(nodeValues[0]));
      queue.offer(root);
      
      for (int i = 1; i < nodeValues.length; i++) {
          TreeNode node = queue.poll();
          if (!nodeValues[i].equals("#")) {
              node.left = new TreeNode(Integer.valueOf(nodeValues[i]));
              queue.offer(node.left);
          }
          if (!nodeValues[++i].equals("#")) {
              node.right = new TreeNode(Integer.valueOf(nodeValues[i]));
              queue.offer(node.right);
          }
      }
      
      return root;
  }
}


public class Codec {
    
  // Encodes a tree to a single string.
  public String serialize(TreeNode root) {      
      StringBuilder sb = new StringBuilder();
      serializeHelper(root, sb);
      return sb.toString();
  }
  
  private void serializeHelper(TreeNode root, StringBuilder sb) {
      if (root != null) {
          sb.append(root.val).append(" ");
          serializeHelper(root.left, sb);
          serializeHelper(root.right, sb);
      } else {
          sb.append("# ");
      }
  }

  // Decodes your encoded data to tree.
  public TreeNode deserialize(String data) {
      List<String> nodeValueList = new LinkedList(Arrays.asList(data.split(" ")));
      return deserializeHelper(nodeValueList);
  }
  
  private TreeNode deserializeHelper(List<String> nodeValueList) {
      String nodeValue = nodeValueList.remove(0);
      if (nodeValue.equals("#")) {
          return null;
      }
      
      TreeNode root = new TreeNode(Integer.valueOf(nodeValue));
      root.left = deserializeHelper(nodeValueList);
      root.right = deserializeHelper(nodeValueList);
      
      return root;
  }
}

