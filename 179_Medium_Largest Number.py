class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort_compare(str: a, str: b) -> int:
            if a + b > b + a:
                return 1
            if a + b < b + a:
                return -1

            return 0

        nums_str = [str(num) for num in nums]
        nums_str = sorted(nums_str, cmp_to_key=(sort_compare))

        if nums_str[0] == "0":
            return "0"

        return "".join([num for num in nums_str])
