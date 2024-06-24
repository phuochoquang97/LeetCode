class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()  # to store the maximums
        min_deque = deque()  # to store the minimums
        left = 0  # left pointer of the sliding window
        max_len = 0  # the length of the longest valid subarray

        for right in range(len(nums)):
            while max_deque and nums[right] > max_deque[-1]:
                max_deque.pop()
            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()

            max_deque.append(nums[right])
            min_deque.append(nums[right])

            # Ensure the difference between the maximum and minimum is within the limit
            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1  # shrink the window from the left

            # Update the length of the longest valid subarray
            max_len = max(max_len, right - left + 1)

        return max_len
