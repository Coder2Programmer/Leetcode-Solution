class Solution:
    def customSortString(self, S: str, T: str) -> str:
        order_dict = {c: i for i, c in enumerate(S)}
        return ''.join(sorted(list(T), key=lambda c: order_dict.get(c, 0)))