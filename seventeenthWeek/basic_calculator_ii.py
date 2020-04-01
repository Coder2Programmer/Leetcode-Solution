class Solution:
    def calculate(self, s: str) -> int:
        sign_set = set(['+', '-', '*', '/'])
        number, sign = 0, '+'
        stack = []
        for i, c in enumerate(s):
            if c.isdigit():
                number = number * 10 + int(c)
            if c not in sign_set and i < len(s) - 1:
                continue
            if sign == '+':
                stack.append(number)
            elif sign == '-':
                stack.append(-number)
            elif sign == '*':
                stack.append(stack.pop() * number)
            else:
                stack.append(int(stack.pop() / number))
            sign = c
            number = 0
            
        return sum(stack)