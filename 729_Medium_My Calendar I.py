class MyCalendar:

    def __init__(self):
        self.time_line = []
        self.second_element = []

    def book(self, start: int, end: int) -> bool:
        if not self.time_line:
            self.time_line.append((start, end))
            # print(self.time_line)
            return True
        # i = 0
        # while  i < len(self.time_line) and self.time_line[i][1] <= start:
        # i += 1
        second_element = [t[1] for t in self.time_line]
        i = bisect.bisect_right(second_element, start)
        # print(f"i: {i}")

        if i == 0:
            if end <= self.time_line[0][0]:
                self.time_line.insert(0, (start, end))
                # print(self.time_line)
                return True
        elif i == len(self.time_line):
            self.time_line.append((start, end))
            # print(self.time_line)
            return True
        elif self.time_line[i - 1][1] <= start and end <= self.time_line[i][0]:
            self.time_line.insert(i, (start, end))
            # print(self.time_line)
            return True

        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
