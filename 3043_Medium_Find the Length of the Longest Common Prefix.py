class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # bruteforce:
        # for each number in arr1:
        #     for each number in arr2:
        #         find the common prefix of a1 and a2
        #         max_len = max(max_len, current_prefix)
        # arr1 and arr2 can contain duplicates -> set()
        # loop -> O(n^2)
        # find common prefix -> need to optimize this -> O(log(len(string)))
        # -> O(n^2log(n))

        # convert to set
        arr1 = sorted(list(set(arr1)), key=lambda x: len(str(x)), reverse=True)
        arr2 = sorted(list(set(arr2)), key=lambda x: len(str(x)), reverse=True)
        # print(arr1)
        # print(arr2)

        def find_common(s1, s2):
            min_len = min(len(s1), len(s2))
            l = 0
            r = min_len - 1
            while l <= r:
                mid = l + (r - l) // 2
                if s1[: mid + 1] == s2[: mid + 1]:
                    l = mid + 1
                else:
                    r = mid - 1

            return l

        ret = 0
        for i in range(len(arr1)):
            a1 = str(arr1[i])
            for j in range(len(arr2)):

                a2 = str(arr2[j])
                if ret >= max(len(a1), len(a2)):
                    return ret
                common_len = find_common(a1, a2)
                # print(f"a1: {a1}, a2: {a2}, find_common: {common_len}")
                ret = max(ret, common_len)

        return ret
