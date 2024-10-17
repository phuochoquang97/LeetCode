class Solution:
    def maximumSwap(self, num: int) -> int:
        def swap_to_max(num_substr):
            num_substr = list(num_substr)
            max_num = num_substr[0]
            max_idx = -1

            # find the index of digit that could be swapped
            for i in range(1, len(num_substr)):
                if num_substr[i] >= max_num:
                    max_num = num_substr[i]
                    max_idx = i

            if max_num == num_substr[0]:  # no swap
                return num_substr

            temp = num_substr[0]
            num_substr[0] = num_substr[max_idx]
            num_substr[max_idx] = temp

            return "".join(num_substr)

        num_str_list = list(str(num))
        num_str_list_sorted = sorted(num_str_list, reverse=True)

        for i in range(len(num_str_list)):
            if num_str_list[i] == num_str_list_sorted[i]:
                continue

            left = "".join(num_str_list[:i])
            right = swap_to_max(num_str_list[i:])
            # print(left, right)
            return int(left + right)

        return num
