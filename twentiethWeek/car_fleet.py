class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target-position)/speed for position, speed in sorted(zip(position, speed))]
        result = cur_time = 0
        for time in reversed(times):
            if time > cur_time:
                result += 1
                cur_time = time
        return result