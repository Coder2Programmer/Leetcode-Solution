class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == '+':
                stack.append(stack[-2]+stack[-1])
            elif op == 'D':
                stack.append(stack[-1]*2)
            else:
                stack.append(int(op))
        return sum(stack)