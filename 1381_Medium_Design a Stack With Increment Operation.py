class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.store = []

    def push(self, x: int) -> None:
        if len(self.store) < self.max_size:
            self.store.append(x)

    def pop(self) -> int:
        if self.store:
            return self.store.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.store))):
            self.store[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
