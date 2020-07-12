class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        left = 0
        for c in S:
            if (c == '(' and left > 0) or (c == ')' and left > 1):
                stack.append(c)
            left += (1, -1)[c==')']
        return ''.join(stack)
