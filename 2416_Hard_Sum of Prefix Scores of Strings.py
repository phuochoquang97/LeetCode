class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # for each word in words:
        #     find all prefix of word -> there are len(word) prefix
        #     for each prefix:
        #         count how many word in words has prefix
        #     ret.append(sum of all counts)

        prefix_map = defaultdict(int)
        for word in words:
            for i in range(1, len(word) + 1):
                prefix_map[word[:i]] += 1
        ret = []
        for word in words:
            count = 0
            for i in range(1, len(word) + 1):
                count += prefix_map[word[:i]]
            ret.append(count)

        return ret
