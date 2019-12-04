class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return head;
        }
        
        Node oldNode = head;
        Node newNode = null;
        while (oldNode != null) {
            newNode = new Node(oldNode.val, oldNode.next, null);
            oldNode.next = newNode;
            oldNode = newNode.next;
        }
        
        oldNode = head;
        while (oldNode != null) {
            newNode = oldNode.next;
            newNode.random = oldNode.random == null ? null : oldNode.random.next;
            oldNode = newNode.next;
        }
        
        Node nodeToChange = head;
        Node newHead = head.next;
        while (nodeToChange.next != null) {
            Node nextNode = nodeToChange.next;
            nodeToChange.next = nextNode.next;
            nodeToChange = nextNode;
        }
        return newHead;
    }
}

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return head;
        }
     
        Map<Node, Node> oldNewNodePairs = new HashMap<>();
        Node currentNode = head;
        while (currentNode != null) {
            oldNewNodePairs.put(currentNode, new Node(currentNode.val, null, null));
            currentNode = currentNode.next;
        }
        
        for (Map.Entry<Node, Node> entry : oldNewNodePairs.entrySet()) {
            Node newNode = entry.getValue();
            newNode.next = oldNewNodePairs.get(entry.getKey().next);
            newNode.random = oldNewNodePairs.get(entry.getKey().random);
        }
        
        return oldNewNodePairs.get(head);
    }
}
