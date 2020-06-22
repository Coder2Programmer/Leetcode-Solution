class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.valid_len = N - len(blacklist)
        self.map = {num: None for num in blacklist}
        last = N - 1
        for num in blacklist:
            if num < self.valid_len:
                while last in self.map:
                    last -= 1
                self.map[num] = last
                last -= 1

    def pick(self) -> int:
        number = random.randint(0, self.valid_len-1)
        return self.map.get(number, number)