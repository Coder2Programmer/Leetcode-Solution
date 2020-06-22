class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(s):
            r = 0
            for c in s:
                r = r * 10 + ord(c) - ord('0')
            return r
        num_sum = str2int(num1) + str2int(num2)
        result = ''
        while num_sum:
            result = chr(num_sum % 10 + ord('0')) + result
            num_sum //= 10
        return result or '0'
