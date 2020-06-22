class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def helper(board: str, counter: collections.Counter) -> int:
            if not board:
                return 0
            min_balls, i = 6, 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[i] == board[j]:
                    j += 1
                need_balls = 3 - (j - i)
                if counter[board[i]] >= need_balls:
                    need_balls = 0 if need_balls < 0 else need_balls
                    counter[board[i]] -= need_balls
                    remain_need_balls = helper(board[:i]+board[j:], counter)
                    if remain_need_balls >= 0:
                        min_balls = min(min_balls, need_balls+remain_need_balls)
                    counter[board[i]] += need_balls
                i = j
            return min_balls if min_balls < 6 else -1
        return helper(board, collections.Counter(hand))
    