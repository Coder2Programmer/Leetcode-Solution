class Solution:
    def averave(self, salary: List[int]) -> float:
        min_num, max_num = float('inf'), -float('inf')
        for s in salary:
            min_num, max_num = min(min_num, s), max(max_num, s)
        return (sum(salary) - min_num - max_num) / (len(salary) - 2)
