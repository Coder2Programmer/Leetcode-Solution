class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                number = stack.pop()
                stack.append(stack.pop() - number)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                number = stack.pop()
                stack.append(int(stack.pop() / number))
            else:
                stack.append(int(token))
        return stack[0]