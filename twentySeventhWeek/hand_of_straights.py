class Solution:
    def isNStrainghtHand(self, hand: List[int], W: int) -> bool:
        counter = collections.Counter(hand)
        roots = [n for n in counter if not counter[n-1]]
        for root in roots:
            for i in range(root, root+W)[::-1]:
                if counter[i] < counter[root]:
                    return False
                counter[i] -= counter[root]
                if counter[i] == 0 and counter[i+1] != 0:
                    roots.append(i+1)
        return True
