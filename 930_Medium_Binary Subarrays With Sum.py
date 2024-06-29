class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # h(x) is the number of subarrays with sum <= x
        # numbers of subarrays = h(goal) - h(goal - 1)
        def h(x):
            if x < 0:
                return 0  # no subarray with negative sum

            l = 0
            current_sum = 0
            ret = 0
            for r in range(0, len(nums)):
                current_sum += nums[r]
                while current_sum > x:  # move left pointer to decrease current_sum
                    current_sum -= nums[l]
                    l += 1
                ret += r - l + 1

            return ret

        return h(goal) - h(goal - 1)
