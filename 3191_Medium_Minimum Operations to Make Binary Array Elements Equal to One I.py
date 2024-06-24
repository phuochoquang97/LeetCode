# this problem is the same as 995, except for k = 3
# 995 is a general problem
# O(N * k) ~ O(N)


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        k = 3
        i = 0
        ret = 0
        current_sum = sum(nums)
        while i <= len(nums) - k:
            if nums[i] == 0:
                current_sum -= nums[i] + nums[i + 1] + nums[i + 2]
                # flip
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ret += 1
                # after flip
                current_sum += nums[i] + nums[i + 1] + nums[i + 2]
            if current_sum == len(nums):
                return ret
            if i == len(nums) - k:
                return -1
            i += 1

        return -1
