class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        queries_sorted = sorted(queries, key=lambda x: x[1])
        max_idx = queries_sorted[-1][1]

        ret = []
        store = [0]
        temp = 0

        for i in range(0, max_idx + 1):
            temp = temp ^ arr[i]
            store.append(temp)

        for l, r in queries:
            ret.append(store[r + 1] ^ store[l])

        return ret
