class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        n = len(nums)
        max_val = nums_sorted[-1]
        ret = 0
        i = 0
        while i < n:
            if nums[i] == max_val:  # start to count
                count = 0
                j = i
                while j < n and nums[j] == max_val:
                    j += 1
                ret = max(j - i, ret)
                i = j
            else:
                i += 1

        return ret
