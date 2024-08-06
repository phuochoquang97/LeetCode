class Solution:
    def minimumPushes(self, word: str) -> int:
        # remap keys 2-9 to distinct collections of letters
        # divide set of letters to 2-9 to get min of pushes
        # sort the char freq in desc order

        # pattern: count the frequency and then sort based on value -> O(NlogN)

        char_freq = defaultdict(int)
        for c in word:
            char_freq[c] += 1

        char_freq_sorted = sorted(char_freq.items(), key=lambda x: -x[1])

        count_step = 1
        count_num = 0
        min_push = 0
        for k, v in char_freq_sorted:
            count_num += 1
            min_push += v * count_step
            if count_num == 8:
                count_num = 0
                count_step += 1

        return min_push
