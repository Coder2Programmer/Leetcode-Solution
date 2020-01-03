class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda pair: (-pair[0], pair[1]))
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue
