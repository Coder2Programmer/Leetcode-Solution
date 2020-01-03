class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = list(collections.Counter(tasks).values())
        max_task = max(task_count)
        max_task_count = task_count.count(max_task)
        return max(len(tasks), (max_task - 1) * (n + 1) + max_task_count)
