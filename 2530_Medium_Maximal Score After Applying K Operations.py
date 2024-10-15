class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ret = 0
        neg_nums = [-num for num in nums]  # simulate max_heap
        heapq.heapify(neg_nums)
        for _ in range(k):
            current_max = heapq.heappop(neg_nums)
            ret -= current_max
            heapq.heappush(neg_nums, -(math.ceil((-current_max) / 3)))

        return ret
