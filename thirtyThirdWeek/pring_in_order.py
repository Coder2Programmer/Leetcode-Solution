class Foo:
    def __init__(self):
        self.s2 = threading.Semaphore(0)
        self.s3 = threading.Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.s2.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.s2:
            printSecond()
        self.s3.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.s3:
            printThird()
