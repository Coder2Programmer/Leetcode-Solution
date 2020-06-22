class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack = []
        index = 0
        while index < len(S):
            level = value = 0
            while S[index] == '-':
                level, index = level+1, index+1
            while index < len(S) and S[index] != '-':
                value, index = value*10+int(S[index]), index+1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(value)
            if stack and stack[-1].left:
                stack[-1].right = node
            elif stack:
                stack[-1].left = node
            stack.append(node)
        return stack[0]
