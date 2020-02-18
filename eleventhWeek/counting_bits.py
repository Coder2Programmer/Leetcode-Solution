class Solution:
    def countBits(self, num: int) -> List[int]:
        bits_list = [0]
        for i in range(1, num+1):
            bits_list.append(bits_list[i>>1] + (i & 1))
        return bits_list
    