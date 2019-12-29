def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n

    prev = 1
    next = 1
    for i in range(n - 1):
        prev, next = next, prev + next
    return next
