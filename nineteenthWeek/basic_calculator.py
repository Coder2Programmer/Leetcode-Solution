class Solution:
    def calculate(self, s: str) -> int:
        s = '+' + s
        s = s.replace('(', '( + ')
        for c in ('+', '-', ')'):
            s = s.replace(c, ' ' + c + ' ')
        
        sign, num = [], []
        result = 0
        for x in s.split():
            if x == '(':
                num.append(result)
                result = 0
            elif x in ('+', '-'):
                sign.append((-1, 1)[x=='+'])
            elif x == ')':
                result *= sign.pop()
                result += num.pop()
            else:
                result += int(x) * sign.pop()
                
        return result