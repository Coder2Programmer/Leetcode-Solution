class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        counter = collections.Counter()
        for word in words:
            if len(set(word)) > 7:
                continue
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - 97)
            counter[mask] += 1
        
        valids = []
        for puzzle in puzzles:
            bfs = [1 << (ord(puzzle[0]) - 97)]
            for c in puzzle[1:]
                bfs.extend([mask | 1 << (ord(c)-97) for mask in bfs])
            valids.append(sum(counter[mask] for mask in bfs))
        return valids
        