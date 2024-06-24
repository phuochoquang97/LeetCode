class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        initial_satisfaction = sum(c * (1 - g) for c, g in zip(customers, grumpy))

        extra_satisfaction = sum(
            c * g for c, g in zip(customers[:minutes], grumpy[:minutes])
        )
        max_extra_satisfaction = extra_satisfaction

        # sliding window
        for i in range(minutes, len(customers)):
            extra_satisfaction += (
                customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
            )
            max_extra_satisfaction = max(max_extra_satisfaction, extra_satisfaction)

        return initial_satisfaction + max_extra_satisfaction


# First approach
class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)
        max_window = 0
        count_one = 0
        start_window = -minutes - 1
        for i in range(0, n - minutes + 1):
            current_window = 0
            current_count_one = 0
            for j in range(i, i + minutes):
                current_window += customers[j]
                current_count_one += grumpy[j] * customers[j]
            if current_count_one == 0:
                continue
            else:
                if current_count_one > count_one:
                    max_window = current_window
                    count_one = current_count_one
                    start_window = i
                elif current_count_one == count_one:
                    if current_window > max_window:
                        max_window = current_window
                        start_window = i
            # print(max_window, start_window)

        total_customer = max_window

        for i in range(0, n):
            if i in range(start_window, start_window + minutes):
                continue
            total_customer += customers[i] * (grumpy[i] ^ 1)

        return total_customer
