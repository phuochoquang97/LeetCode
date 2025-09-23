class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        store = []
        if m == 0:
            store = nums2.copy()
        if n == 0:
            store = nums1.copy()
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                store.append(nums1[i])
                i += 1
                if i == m:
                    store.extend(nums2[j:])
                    break
            else:
                store.append(nums2[j])
                j += 1
                if j == n:
                    store.extend(nums1[i:])
                    break
        med_index = (m + n) // 2
        if (m + n) % 2 == 0:
            return (store[med_index - 1] + store[med_index]) / 2
        else:
            return store[med_index]
