class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # nums: array int, len n <= 1000
        # compute sum of non-empty continuous subarrays
        # sort the sum
        # sum of sum_array[left:right] inclusive

        cum_sum = []
        current_cum_sum = 0
        for num in nums:  # O(n)
            current_cum_sum += num
            cum_sum.append(current_cum_sum)

        sum_subarrays = []
        for i in range(len(cum_sum)):  # O(n^2)
            sum_subarrays.append(cum_sum[i])
            for j in range(i + 1, len(cum_sum)):
                sum_subarrays.append(cum_sum[j] - cum_sum[i])

        sum_subarrays.sort()  # O(nlogn)
        ret = 0
        for i in range(left - 1, right):  # O(n)
            ret = (ret + sum_subarrays[i] % (10**9 + 7)) % (10**9 + 7)

        return ret  # O(n)
