class Solution:
    def myAtoi(self, s: str) -> int:
        lst = list(s.strip())
        if len(lst) == 0:
            return 0
        sign = (1, -1)[lst[0] == '-']
        i = int(lst[0] in ('-', '+'))
        ans = 0
        while i < len(lst) and lst[i].isdigit():
            ans = ans * 10 + ord(lst[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign*ans, 2**31-1))
