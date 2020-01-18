class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_one = []
        self.stack_two = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_one.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_two:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())
        return self.stack_two.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack_two[-1] if self.stack_two else self.stack_one[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_one and not self.stack_two
