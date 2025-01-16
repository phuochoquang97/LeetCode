class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)

        def xor_of_list(nums):
            ret = 0
            for num in nums:
                ret ^= num
            return ret

        if len1 % 2 == 0:
            if len2 % 2 != 0:
                return xor_of_list(nums1)
            else:
                return 0
        else:
            if len2 % 2 == 0:
                return xor_of_list(nums2)
            else:
                return xor_of_list(nums1 + nums2)

        return 0
