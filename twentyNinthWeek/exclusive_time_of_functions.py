class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        prev_t = 0
        for log in logs:
            func_id, kind, t = log.split(':')
            func_id, t = int(func_id), int(t)
            if kind == 'start':
                if stack:
                    result[stack[-1]] += t - prev_t
                stack.append(func_id)
                prev_t = t
            else:
                result[stack.pop()] += t - prev_t + 1
                prev_t = t + 1
        return result
    