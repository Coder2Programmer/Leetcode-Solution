class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = collections.Counter(S)
        heap = [(-count, char) for char, count in counter.items()]
        heapq.heapify(heap)
        prev_count, prev_char = 0, ''
        result = []
        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            count += 1
            prev_count, prev_char = count, char
        return ''.join(result) if len(result) == len(S) else ''
        