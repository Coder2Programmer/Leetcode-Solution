class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        left_stack, right_stack = [root], []
        while left_stack:
            level = []
            while left_stack:
                node = left_stack.pop()
                level.append(node.val)
                if node.left:
                    right_stack.append(node.left)
                if node.right:
                    right_stack.append(node.right)
            result.append(level)
            
            if not right_stack:
                break
            level = []
            while right_stack:
                node = right_stack.pop()
                level.append(node.val)
                if node.right:
                    left_stack.append(node.right)
                if node.left:
                    left_stack.append(node.left)
            result.append(level)
        return result


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:    
        if not root:
            return []
        
        result = []
        queue = collections.deque()
        queue.append(root)
        left_to_right = True
        while queue:
            size = len(queue)
            level = [None] * size
            for i in range(size):
                node = queue.popleft()
                index =  i if left_to_right else size - i - 1
                level[index] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            left_to_right = not left_to_right
            result.append(level)
        return result