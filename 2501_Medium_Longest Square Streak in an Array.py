class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(nums)
        map_count = defaultdict(int)

        for num in nums:
            squared = math.sqrt(num)
            if squared in map_count.keys():
                map_count[num] = map_count[squared] + 1
            else:
                map_count[num] = 1
        # print(map_count)

        sorted_len = sorted(map_count.values(), reverse=True)

        return sorted_len[0] if sorted_len[0] != 1 else -1
