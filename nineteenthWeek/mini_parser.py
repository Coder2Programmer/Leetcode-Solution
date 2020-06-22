class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def helper(chars: list) -> NestedInteger:
            num = ''
            while chars[-1] in '-0123456789':
                num += chars.pop()
            if num:
                return NestedInteger(int(num))
            chars.pop()
            list_ = NestedInteger()
            while chars[-1] != ']':
                list_.add(helper(chars))
                if chars[-1] == ',':
                    chars.pop()
            chars.pop()
            return list_
        chars = list(' ' + s[::-1])
        return helper(chars)
    