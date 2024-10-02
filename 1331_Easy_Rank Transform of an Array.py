class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ret = []
        if not arr:
            return ret

        arr_sorted = sorted(arr)

        rank_map = defaultdict(int)
        current_rank = 1
        current_val = arr_sorted[0]

        rank_map[current_val] = current_rank

        for i in range(1, len(arr_sorted)):
            if arr_sorted[i] == current_val:
                rank_map[arr_sorted[i]] = current_rank
            else:
                current_rank += 1
                rank_map[arr_sorted[i]] = current_rank
                current_val = arr_sorted[i]

        for a in arr:
            ret.append(rank_map[a])

        return ret
