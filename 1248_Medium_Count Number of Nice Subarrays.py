class Solution:
    def numberOfSubarrays(self, nums: List[int], goal: int) -> int:
        nums = [num % 2 for num in nums]

        def h(x):
            if x < 0:
                return 0

            l, current_sum = 0
            ret = 0
            for r in range(len(nums)):
                current_sum += nums[r]

                while current_sum > x:
                    current_sum -= nums[l]
                    l += 1

                ret += r - l + 1

            return ret

        return h(goal) - h(goal - 1)
