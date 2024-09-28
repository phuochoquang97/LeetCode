class MyCalendarTwo:

    def __init__(self):
        self.single = []
        self.double = []

    def book(self, start: int, end: int) -> bool:
        # find single conflict with current event
        conflict = set()
        for i in range(len(self.single)):
            s_event, e_event = self.single[i]
            if (start in range(s_event, e_event)) or s_event in range(start, end):
                conflict.add((max(start, s_event), min(end, e_event)))
        # print(f"conflict: {conflict}")
        for s_c, e_c in conflict:
            for s_event, e_event in self.double:
                if (s_c in range(s_event, e_event)) or (s_event in range(s_c, e_c)):
                    return False

        # update single and double
        self.single.append((start, end))
        self.double.extend(conflict)
        # print(f"single: {self.single}")
        # print(f"double: {self.double}")
        # print("---------")
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
