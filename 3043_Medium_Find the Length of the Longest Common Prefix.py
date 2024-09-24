class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ret = 0
        s1 = set()
        for i in range(len(arr1)):
            a1 = str(arr1[i])
            for j in range(1, len(a1) + 1):
                s1.add(a1[:j])
        s2 = set()
        for i in range(len(arr2)):
            a2 = str(arr2[i])
            for j in range(1, len(a2) + 1):
                s2.add(a2[:j])

        for e in s1:
            if e in s2:
                ret = max(ret, len(e))
        return ret
