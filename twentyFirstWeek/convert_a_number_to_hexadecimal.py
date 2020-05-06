class Solution:
    def toHex(self, num: int) -> str:
        char_map = ['0', '1', '2', '3', '4', '5', '6', '7',
                    '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        result, num = '', num & 0xFFFFFFFF
        while num:
            result = char_map[num&0xF] + result
            num >>= 4
        return result or '0'
    