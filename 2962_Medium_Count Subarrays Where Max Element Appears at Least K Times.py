class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        n = len(nums)
        nb_max = 0
        nb_subarrays = 0
        right = 0

        for left in range(n):
            while right < n and nb_max < k:
                if nums[right] == max_val:
                    nb_max += 1
                right += 1
            
            if nb_max >= k:
                nb_subarrays += n - right + 1
            
            if nums[left] == max_val:
                nb_max -= 1
        
        return nb_subarrays